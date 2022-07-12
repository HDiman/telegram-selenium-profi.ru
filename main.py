from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time
from get_info import *


# Link to Main Webpage
url = "https://profi.ru/backoffice/n.php"

# Entering inside the Main page

try:
    # Enter main page
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
    # print(chat_order)
    time.sleep(5)

    # inside chat
    driver.get(url=chat_order)
    time.sleep(5)

    # Get info about Request Orders
    get_info("-- Открытые ордера --")

    # ===========================================
    # Find out href link to pass for Waiting Order
    waiting_order = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/a[2]").get_attribute('href')
    # print(waiting_order)
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


# finally:
#     driver.close()
#     driver.quit()
