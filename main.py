from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time
from get_info import *
from enter_web_page import *


enter_page()

try:
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


finally:
    driver.close()
    driver.quit()
