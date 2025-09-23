#!/usr/bin/env python3
"""Gera o site estático a partir de NOTEBOOK.md."""
from __future__ import annotations

import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re

try:
    import markdown  # type: ignore
except ModuleNotFoundError as exc:  # pragma: no cover - feedback amigável
    sys.exit(
        "Dependência 'markdown' não encontrada. Execute 'python -m pip install -r requirements.txt' "
        "dentro do ambiente virtual antes de gerar o site."
    )

ROOT_DIR = Path(__file__).resolve().parents[1]
SOURCE_MD = ROOT_DIR / "NOTEBOOK.md"
TEMPLATE_FILE = ROOT_DIR / "templates" / "base.html"
ASSETS_DIR = ROOT_DIR / "assets"
OUTPUT_DIR = ROOT_DIR / "public"


DIRECTIVE_PATTERN = re.compile(
    r"\{\{\s*(?P<name>[a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*(?P<body>[^}]+?)\s*\}\}"
)
BACK_LINK_HTML = '<p class="back-link"><a href="index.html">&larr; Voltar</a></p>'


@dataclass
class DetailPage:
    """Metadados para páginas auxiliares geradas a partir de markdown."""

    source_path: Path
    output_rel_path: Path
    label: str
    title: str | None = None


def render_markdown(markdown_text: str) -> tuple[str, str]:
    """Converte markdown em HTML e devolve também o TOC gerado."""

    md_converter = markdown.Markdown(
        extensions=[
            "toc",
            "fenced_code",
            "tables",
            "codehilite",
            "attr_list",
            "sane_lists",
        ]
    )

    html = md_converter.convert(markdown_text)
    toc_html = md_converter.toc or ""
    return html, toc_html


def extract_first_heading(markdown_text: str) -> str | None:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("# ")
    return None


def process_markdown(markdown_text: str) -> tuple[str, list[DetailPage]]:
    """Processa diretivas personalizadas e devolve markdown atualizado."""

    detail_pages: dict[str, DetailPage] = {}

    def replace(match: re.Match[str]) -> str:
        name = match.group("name")
        body = match.group("body")
        if name == "include":
            relative_path = body.strip().strip("\"'")
            include_path = (ROOT_DIR / relative_path).resolve()

            try:
                include_path.relative_to(ROOT_DIR)
            except ValueError as exc:  # pragma: no cover - validação defensiva
                raise ValueError(
                    f"Include fora do diretório do projeto: {relative_path}"
                ) from exc

            if not include_path.exists():
                raise FileNotFoundError(f"Include não encontrado: {relative_path}")

            return include_path.read_text(encoding="utf-8")

        if name == "include_page":
            segments = [
                segment.strip() for segment in body.split("|") if segment.strip()
            ]
            if not segments:
                raise ValueError("Diretiva include_page sem caminho")

            relative_path_raw = segments[0].strip().strip("\"'")
            include_path = (ROOT_DIR / relative_path_raw).resolve()

            try:
                include_path.relative_to(ROOT_DIR)
            except ValueError as exc:  # pragma: no cover - validação defensiva
                raise ValueError(
                    f"Include fora do diretório do projeto: {relative_path_raw}"
                ) from exc

            if not include_path.exists():
                raise FileNotFoundError(f"Include não encontrado: {relative_path_raw}")

            options: dict[str, str] = {}
            for segment in segments[1:]:
                if "=" not in segment:
                    continue
                key, value = segment.split("=", 1)
                options[key.strip()] = value.strip().strip("\"'")

            label = options.get("label") or Path(relative_path_raw).stem
            title = options.get("title")
            output_hint = options.get("output")
            if output_hint:
                output_rel_path = Path(output_hint)
            else:
                source_parts = include_path.relative_to(ROOT_DIR).with_suffix("").parts
                safe_name = "-".join(source_parts)
                output_rel_path = Path(f"{safe_name}.html")

            if output_rel_path.is_absolute():
                raise ValueError(
                    f"O caminho de saída deve ser relativo: {output_rel_path}"
                )

            output_rel_posix = output_rel_path.as_posix()
            detail_page = detail_pages.get(output_rel_posix)
            if detail_page is None:
                detail_pages[output_rel_posix] = DetailPage(
                    source_path=include_path,
                    output_rel_path=output_rel_path,
                    label=label,
                    title=title,
                )
            else:
                if detail_page.source_path != include_path:
                    raise ValueError(
                        "Duas diretivas include_page com o mesmo output apontam para arquivos diferentes"
                    )
                if title and detail_page.title is None:
                    detail_page.title = title

            return f"[{label}]({output_rel_posix})"

        raise ValueError(f"Diretiva desconhecida: {name}")

    previous = None
    current = markdown_text
    while previous != current:
        previous = current
        current = DIRECTIVE_PATTERN.sub(replace, current)

    return current, list(detail_pages.values())


def build_site() -> None:
    if not SOURCE_MD.exists():
        raise FileNotFoundError(f"Ficheiro fonte não encontrado: {SOURCE_MD}")

    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError(f"Template base não encontrado: {TEMPLATE_FILE}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Limpa build anterior para garantir assets sincronizados
    for item in OUTPUT_DIR.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

    raw_markdown = SOURCE_MD.read_text(encoding="utf-8")
    processed_markdown, detail_pages = process_markdown(raw_markdown)
    template_html = TEMPLATE_FILE.read_text(encoding="utf-8")

    rendered_html, toc_html = render_markdown(processed_markdown)

    main_last_updated = datetime.fromtimestamp(SOURCE_MD.stat().st_mtime).strftime(
        "%d/%m/%Y %H:%M"
    )
    generated_at = datetime.now().strftime("%d/%m/%Y %H:%M")

    page_html = template_html
    page_html = page_html.replace("{{ content }}", rendered_html)
    page_html = page_html.replace("{{ toc }}", toc_html)
    page_html = page_html.replace("{{ last_updated }}", main_last_updated)
    page_html = page_html.replace("{{ generated_at }}", generated_at)
    page_html = page_html.replace("{{ page_title }}", "Notebook")

    OUTPUT_DIR.joinpath("index.html").write_text(page_html, encoding="utf-8")

    for detail in detail_pages:
        detail_markdown = detail.source_path.read_text(encoding="utf-8")
        detail_html, detail_toc = render_markdown(detail_markdown)
        detail_last_updated = datetime.fromtimestamp(
            detail.source_path.stat().st_mtime
        ).strftime("%d/%m/%Y %H:%M")
        detail_title = (
            detail.title or extract_first_heading(detail_markdown) or detail.label
        )

        detail_page_html = template_html
        detail_content = f"{BACK_LINK_HTML}\n{detail_html}"
        detail_page_html = detail_page_html.replace("{{ content }}", detail_content)
        detail_page_html = detail_page_html.replace("{{ toc }}", detail_toc)
        detail_page_html = detail_page_html.replace(
            "{{ last_updated }}", detail_last_updated
        )
        detail_page_html = detail_page_html.replace("{{ generated_at }}", generated_at)
        detail_page_html = detail_page_html.replace("{{ page_title }}", detail_title)

        output_path = OUTPUT_DIR / detail.output_rel_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(detail_page_html, encoding="utf-8")

    if ASSETS_DIR.exists():
        shutil.copytree(ASSETS_DIR, OUTPUT_DIR / "assets")

    print(f"Site gerado em: {OUTPUT_DIR / 'index.html'}")


def main() -> None:
    try:
        build_site()
    except Exception as error:  # pragma: no cover - execução via CLI
        sys.exit(f"Erro ao gerar o site: {error}")


if __name__ == "__main__":
    main()
