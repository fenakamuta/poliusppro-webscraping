import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/page/2"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    for quote in soup.select(".quote"):
        a_tag = quote.find("a")
        if a_tag:
            print(a_tag.get("href"))
else:
    print("Erro ao acessar a página:", response.status_code)
