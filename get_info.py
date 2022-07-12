from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time

# Path to chromedriver
chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/telegram-selenium-profi.ru/driver/chromedriver"
# Options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
# Creating Driver Object
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


# Getting information about orders
def get_info(order_name):
    clients_order = driver.find_elements(By.CLASS_NAME, "client-info__name")
    dates_order = driver.find_elements(By.CLASS_NAME, "lbl")
    addresses_order = driver.find_elements(By.XPATH, "//div[@title='Район']")
    subjects_order = driver.find_elements(By.CLASS_NAME, "subjects")
    descriptions_order = driver.find_elements(By.CLASS_NAME, "aim")
    prices_order = driver.find_elements(By.XPATH, "//div[@title='Ставка']")
    for n in range(len(clients_order)):
        print(f"\n{order_name}\n"
              f"клиент: {clients_order[n].text}\n"
              f"заказ от: {dates_order[n].text}\n"
              f"адрес: {addresses_order[n].text}\n"
              f"тема: {subjects_order[n].text}\n"
              f"проблема: {descriptions_order[n].text}")
        if order_name == "-- В работе --":
            print(f"стоимость заказа: {prices_order[n].text}\n")
        time.sleep(5)