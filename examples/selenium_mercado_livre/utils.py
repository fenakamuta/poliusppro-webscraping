import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_selenium_driver():
    chrome_options = Options()
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    )
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/google-chrome"  # Adjust if necessary
    webdriver_service = Service()
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    return driver


def make_search(driver, search_text, search_input_selector, search_button_selector):
    wait = WebDriverWait(driver, 15)
    item_search_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, search_input_selector))
    )
    item_search_input.click()
    time.sleep(1)

    item_search_input.clear()
    item_search_input.send_keys(search_text)

    time.sleep(1)
    search_button_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, search_button_selector))
    )
    search_button_element.click()


def get_card_items(cards):
    itens = []
    for card in cards:
        try:
            # Título e link (dentro do elemento <h3> que contém um <a>)
            titulo_elem = card.find_element(
                By.CSS_SELECTOR, "h3.poly-component__title-wrapper a"
            )
            titulo = titulo_elem.text
            link = titulo_elem.get_attribute("href")
        except Exception:
            titulo, link = "", ""

        try:
            # Preço: pode ser extraído de um container de preço
            preco_elem = card.find_element(By.CSS_SELECTOR, "div.poly-component__price")
            preco = preco_elem.text
        except Exception:
            preco = ""

        try:
            # Frete ou shipping, se disponível
            shipping_elem = card.find_element(
                By.CSS_SELECTOR, "div.poly-component__shipping"
            )
            shipping = shipping_elem.text
        except Exception:
            shipping = ""

        try:
            # Review (rating) do item
            review_elem = card.find_element(
                By.CSS_SELECTOR, "span.poly-reviews__rating"
            )
            review = review_elem.text
        except Exception:
            review = ""

        try:
            # Número de avaliações
            reviews_total_elem = card.find_element(
                By.CSS_SELECTOR, "span.poly-reviews__total"
            )
            numero_avaliacoes = reviews_total_elem.text.strip()
        except Exception:
            numero_avaliacoes = ""

        itens.append(
            {
                "titulo": titulo,
                "link": link,
                "preco": preco,
                "shipping": shipping,
                "review": review,
                "numero_avaliacoes": numero_avaliacoes,
            }
        )
    return itens
