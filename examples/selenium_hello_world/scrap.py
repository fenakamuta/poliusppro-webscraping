from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")


# 1) Clique básico com time sleep
time.sleep(2)
selector = "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.RNmpXc"
driver.find_element(By.CSS_SELECTOR, selector).click()
time.sleep(5)


# 2) Esperando o elemento ficar disponível
wait = WebDriverWait(driver, 15)
selector = "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.RNmpXc"
button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
button.click()
time.sleep(5)

# 3) Pegando itens
wait = WebDriverWait(driver, 15)
button_selector = "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.RNmpXc"
button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, button_selector)))
button.click()

carousel_selector = ".brand-accent-1 .glue-carousel__item .doodle-card-wrapper"
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, carousel_selector)))
carousel_items = driver.find_elements(By.CSS_SELECTOR, carousel_selector)

world_events = []
for carousel_item in carousel_items:
    date = carousel_item.find_element(
        By.CSS_SELECTOR, ".doodle-card-content__date"
    ).text
    event = carousel_item.find_element(
        By.CSS_SELECTOR, ".doodle-card-content__event"
    ).text
    if date and event:
        world_events.append((date, event))

from pprint import pprint

pprint(world_events)
