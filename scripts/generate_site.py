#!/usr/bin/env python3
"""Gera o site estático a partir de NOTEBOOK.md."""
from __future__ import annotations

import shutil
import sys
from datetime import datetime
from pathlib import Path

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
    template_html = TEMPLATE_FILE.read_text(encoding="utf-8")

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

    rendered_html = md_converter.convert(raw_markdown)
    toc_html = md_converter.toc or ""

    last_updated = datetime.fromtimestamp(SOURCE_MD.stat().st_mtime).strftime("%d/%m/%Y %H:%M")
    generated_at = datetime.now().strftime("%d/%m/%Y %H:%M")

    page_html = template_html
    page_html = page_html.replace("{{ content }}", rendered_html)
    page_html = page_html.replace("{{ toc }}", toc_html)
    page_html = page_html.replace("{{ last_updated }}", last_updated)
    page_html = page_html.replace("{{ generated_at }}", generated_at)

    OUTPUT_DIR.joinpath("index.html").write_text(page_html, encoding="utf-8")

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
