from get_info import *


def enter_page():
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