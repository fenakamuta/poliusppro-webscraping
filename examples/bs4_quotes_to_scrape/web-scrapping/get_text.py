import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    for text in soup.select(".quote span.text"):
        print(text.get_text())
else:
    print("Erro ao acessar a página:", response.status_code)
