import os
import time


import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def parse_page(driver):
    products = []
    cards = driver.find_elements(By.CSS_SELECTOR, "div.card_v2-product--wrapper")

    for card in cards:
        name = card.find_element(By.CSS_SELECTOR, "div.card_v2-product-name a").text.strip()
        
        price = card.find_element(By.CSS_SELECTOR, "div.card_v2-product-price").text
        price = ''.join(filter(str.isdigit, price))
        
        try:
            reviews = card.find_element(By.CSS_SELECTOR, "div.card_v2-product-shape").text
            reviews = ''.join(filter(str.isdigit, reviews))
        except:
            reviews = "0"
        
        try:
            rating = card.find_element(By.CSS_SELECTOR, "div.card_v2-product-star").text
        except:
            rating = "0"
        
        products.append([name, price, reviews, rating])
    
    return products


def parser_cccstore(pages=1):
    compnet_profile = r"C:\compnet_profile"   # Отдельный профиль Chrome для этого предмета
    if not os.path.exists(compnet_profile):
        os.makedirs(compnet_profile)

    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={compnet_profile}")   # Использует этот профиля
    options.add_argument("--profile-directory=Default")          # Использует этот подпрофиль
    options.page_load_strategy = 'eager'                         # Загружает только html страницы

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    products = []

    for page in range(1, pages+1):
        if page == 1:
            url = "https://cccstore.ru/catalog/kubiki-rubika/"
        else:
            url = f"https://cccstore.ru/catalog/kubiki-rubika/?PAGEN_1={page}"

        print(f"Открываем страницу {page}...")
        driver.get(url)
        time.sleep(5)

        products.extend(parse_page(driver))
        print(f"Всего найдено товаров: {len(products)}\n")

    driver.quit()
    return products


if __name__ == "__main__":
    df = pd.DataFrame(parser_cccstore(5), columns=['name', 'price', 'reviews', 'rating'])
    df.index = range(1, len(df) + 1)
    df.to_csv('info.csv')