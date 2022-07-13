from enter_profi import *


# Getting information about orders
def get_info(order_name):
    order_dict = {}
    clients_order = driver.find_elements(By.CLASS_NAME, "client-info__name")
    dates_order = driver.find_elements(By.CLASS_NAME, "lbl")
    addresses_order = driver.find_elements(By.XPATH, "//div[@title='Район']")
    subjects_order = driver.find_elements(By.CLASS_NAME, "subjects")
    descriptions_order = driver.find_elements(By.CLASS_NAME, "aim")
    prices_order = driver.find_elements(By.XPATH, "//div[@title='Ставка']")
    # for n in range(len(clients_order)):
    #     print(f"\n{order_name}\n"
    #           f"клиент: {clients_order[n].text}\n"
    #           f"заказ от: {dates_order[n].text}\n"
    #           f"адрес: {addresses_order[n].text}\n"
    #           f"тема: {subjects_order[n].text}\n"
    #           f"проблема: {descriptions_order[n].text}")
    #     if order_name == "-- В работе --":
    #         print(f"стоимость заказа: {prices_order[n].text}\n")
    #     time.sleep(5)

    for n in range(len(clients_order)):
        order_dict = {
            "ордер:": order_name,
            "клиент:": clients_order[n].text,
            "заказ от:": dates_order[n].text,
            "адрес:": addresses_order[n].text,
            "тема:": subjects_order[n].text,
            "проблема:": descriptions_order[n].text
            }
        if order_name == "-- В работе --":
            order_dict["стоимость заказа:"] = prices_order[n].text

    return order_dict


def working_orders():
        # ===========================================
        # Find out href link to enter Working Orders
        working_orders = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/a[2]").get_attribute('href')
        # print(working_orders)
        time.sleep(5)

        # inside chat
        driver.get(url=working_orders)
        time.sleep(5)

        # Returning info about Request Orders
        return get_info("-- В работе --")


def open_orders():
        # ===========================================
        # Find out href link to enter Open Orders
        open_orders = driver.find_element(By.ID, "js-tab-orders-repls").get_attribute('href')
        # print(open_orders)
        time.sleep(5)

        # inside chat
        driver.get(url=open_orders)
        time.sleep(5)

        # Returning info from Open Orders
        return get_info("-- Открытые ордера --")
