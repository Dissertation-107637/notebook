# Notebook ➜ GitHub Pages

## Estrutura

- `NOTEBOOK.md`: fonte principal do conteúdo.
- `scripts/generate_site.py`: script que converte o markdown em HTML.
- `templates/base.html`: layout base do site.
- `assets/styles.css`: estilos globais e responsivos.
- `assets/certificates`: certificados.
- `requirements.txt`: dependências Python necessárias para a geração.
- `.github/workflows/deploy.yml`: workflow que trata do build e deploy automático.

## Preparar o ambiente local

1. **Criar ambiente virtual**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate    # Windows PowerShell
   ```
2. **Instalar dependências**
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

## Gerar o site localmente

1. Certifique-se de que o ambiente virtual está ativo.
2. Execute o gerador:
   ```bash
   python scripts/generate_site.py
   ```
3. Abra `public/index.html` no browser ou, se preferir, exponha os ficheiros:
   ```bash
   python -m http.server --directory public 8000
   ```

Sempre que editar `NOTEBOOK.md`, volte a executar o script para validar o resultado antes de fazer commit.

## Fluxo automático com GitHub Pages

1. Faça commit de todos os ficheiros e envie para a branch `main`.
2. No repositório GitHub, abra **Settings → Pages** e, em _Build and deployment_, escolha **GitHub Actions**.
3. O workflow `.github/workflows/deploy.yml` será executado automaticamente em cada push para `main`:
   - Cria um ambiente virtual isolado;
   - Instala as dependências listadas;
   - Converte `NOTEBOOK.md` em `public/index.html` reaproveitando o template e os estilos;
   - Publica o resultado através do GitHub Pages.
4. Assim que o deploy terminar, o GitHub mostrará o URL público do site.

## Personalização

- Altere o layout em `templates/base.html` para ajustar secções, títulos ou textos fixos.
- Adapte a identidade visual editando `assets/styles.css`.
- Adicione novos recursos (imagens, PDFs, etc.) na pasta `assets` — serão copiados automaticamente para `public/assets` durante o build.

Com estes passos, basta manter `NOTEBOOK.md` atualizado para que o site reflita instantaneamente o progresso da tese após cada commit na `main`.
