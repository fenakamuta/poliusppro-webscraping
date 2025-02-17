# PolisUSPPro - Projeto de Web Scraping com Python

## Descrição
Este repositório apresenta exemplos práticos de extração de dados utilizando as bibliotecas BeautifulSoup e Selenium.

## Pré-requisitos
- Python 3.12 ou superior
- pip (ou pip3)
- Ambiente virtual (virtualenv) – recomendado
- Navegador Chrome instalado
- Chromedriver compatível com a versão do Chrome

## Instalação
1. Clone o repositório:
    ```
    git clone git@github.com:fenakamuta/poliusppro-webscraping.git
    ```
2. Acesse o diretório do projeto:
    ```
    cd poliusppro-webscraping
    ```
3. Crie um ambiente virtual:
    ```
    python3 -m venv venv
    ```
   Para ativar o ambiente virtual:
    - No Windows:
      ```
      venv\Scripts\activate
      ```
    - No Linux/macOS:
      ```
      source venv/bin/activate
      ```
4. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```

## Execução
Após a configuração, execute os scripts conforme a necessidade:
```
python examples/bs4_quotes_to_scrape/web-scrapping/get_text.py
python examples/selenium_hello_world/scrap.py
python examples/selenium_mercado_livre/scrap.py
```