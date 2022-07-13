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


# Function to enter Main Page
def enter_web_page():
    # Link to Main Webpage
    url = "https://profi.ru/backoffice/n.php"

    # Entering inside the Main page
    driver.get(url=url)
    time.sleep(5)

    # Enter login with phone number
    login_input = driver.find_element(By.CLASS_NAME, "login-form__input-login")
    login_input.clear()
    login_input.send_keys("+79160585921")
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "login-form__button").click()

    # Input code instead of password
    input_code = input("Please input number: ")
    time.sleep(5)
    for i in range(4):
        enter_code = driver.find_element(By.CLASS_NAME, "ui-pin-input")
        enter_code.send_keys(f"{input_code[i]}")
        time.sleep(2)

    # Inside Main page -> Waiting for page to be downloaded
    time.sleep(30)

# Function to enter Chat
def enter_chat():
    # ===========================================
    # Find out href link to enter Chat Navigation
    chat_order = driver.find_element(By.XPATH, "//*[@id='BO_REACT_MOBILE_TAB_BAR']/nav/a[2]").get_attribute('href')
    # print(chat_order)
    time.sleep(5)

    # Getting inside Chat
    driver.get(url=chat_order)
    time.sleep(5)
