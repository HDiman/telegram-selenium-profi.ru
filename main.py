from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time


# Path to chromedriver
chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/telegram-selenium-head_hunter/driver/chromedriver"
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
        print(f"{order_name}\n"
              f"клиент: {clients_order[n].text}\n"
              f"заказ от: {dates_order[n].text}\n"
              f"адрес: {addresses_order[n].text}\n"
              f"тема: {subjects_order[n].text}\n"
              f"проблема: {descriptions_order[n].text}")
        if order_name == "-- В работе --":
            print(f"стоимость заказа: {prices_order[n].text}\n")
        time.sleep(5)


# Link to Main Webpage
url = "https://profi.ru/backoffice/n.php"

# Entering inside the Main page
try:
    # Enter page
    driver.get(url=url)
    time.sleep(5)

    # Enter login with phone number
    login_input = driver.find_element(By.CLASS_NAME, "login-form__input-login")
    login_input.clear()
    login_input.send_keys("+79160585921")
    time.sleep(5)
    submit_button = driver.find_element(By.CLASS_NAME, "login-form__button").click()

    # Input code instead of password
    input_code = input("Please input number: ")
    time.sleep(5)
    for i in range(4):
        enter_code = driver.find_element(By.CLASS_NAME, "ui-pin-input")
        enter_code.send_keys(f"{input_code[i]}")
        time.sleep(2)

    # Waiting for page downloaded
    time.sleep(30)

    # ===========================================
    # Find out href link to pass for enter inside
    chat_order = driver.find_element(By.XPATH, "//*[@id='BO_REACT_MOBILE_TAB_BAR']/nav/a[2]").get_attribute('href')
    print(chat_order)
    time.sleep(5)

    # inside chat
    driver.get(url=chat_order)
    time.sleep(5)

    # Get info about Request Orders
    get_info("-- Открытые ордера --")

    # ===========================================
    # Find out href link to pass for Waiting Order
    waiting_order = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/a[2]").get_attribute('href')
    print(waiting_order)
    time.sleep(5)

    # inside chat
    driver.get(url=waiting_order)
    time.sleep(5)

    # Get info about Request Orders
    get_info("-- В работе --")

    # # ===========================================
    # # Find out href link to pass for Request Order
    # request_order = driver.find_element(By.ID, "js-tab-orders-repls").get_attribute('href')
    # print(request_order)
    # time.sleep(5)
    #
    # # inside chat
    # driver.get(url=request_order)
    # time.sleep(5)
    #
    # # Get info about Request Orders
    # get_info("Открытые ордера")
    #
    # # ===========================================


    time.sleep(60)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
