import logging
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import SELECTORS, N_PAGES, SEARCH_TEXT, INITIAL_URL
from utils import make_search, get_selenium_driver, get_card_items


def configurar_logger():
    logging.basicConfig(
        level=logging.INFO, format="[%(levelname)s] %(asctime)s - %(message)s"
    )
    return logging.getLogger("webscraping")


def capturar_itens(driver, logger):
    df_itens = pd.DataFrame()
    pages_visited = 0
    wait = WebDriverWait(driver, 15)

    while pages_visited < N_PAGES:
        logger.info(f"Capturando itens: página {pages_visited + 1} de {N_PAGES}")
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS["item_card"]))
        )

        item_cards = driver.find_elements(By.CSS_SELECTOR, SELECTORS["item_card"])
        item_data = get_card_items(item_cards)
        df_itens = pd.concat([df_itens, pd.DataFrame(item_data)], ignore_index=True)
        logger.info("Itens extraídos com sucesso!")
        pages_visited += 1

        try:
            wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, SELECTORS["next_button"])
                )
            )
            next_button = driver.find_element(By.CSS_SELECTOR, SELECTORS["next_button"])
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            next_button.click()
        except Exception as e:
            print(e)
            logger.info("Não há mais páginas disponíveis. Encerrando a extração.")
            break

    return df_itens


def web_scrap_ml_item():
    logger = configurar_logger()
    driver = None
    try:
        logger.info("Iniciando a extração de dados da web")
        driver = get_selenium_driver()
        driver.get(INITIAL_URL)

        make_search(
            driver, SEARCH_TEXT, SELECTORS["search_input"], SELECTORS["search_button"]
        )
        logger.info("Pesquisa realizada - iniciando a captura de itens")
        df_itens = capturar_itens(driver, logger)
    finally:
        if driver:
            driver.quit()
        df_itens.to_csv("itens.csv", index=False)
        logger.info("Dados extraídos salvos em itens.csv")


def main():
    web_scrap_ml_item()


if __name__ == "__main__":
    main()
