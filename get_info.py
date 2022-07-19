from enter_profi import *


# Getting information about orders
def get_info(order_name):
    # global search_list
    clients_order = driver.find_elements(By.CLASS_NAME, "client-info__name")
    if clients_order == []:
        order_list = []
        pass
    else:
        dates_order = driver.find_elements(By.CLASS_NAME, "lbl")
        addresses_order = driver.find_elements(By.XPATH, "//div[@title='Район']")
        subjects_order = driver.find_elements(By.CLASS_NAME, "subjects")
        descriptions_order = driver.find_elements(By.CLASS_NAME, "aim")
        prices_order = driver.find_elements(By.XPATH, "//div[@title='Ставка']")

        # This section for Dictionaries in List
        order_list = []
        # search_list = []
        for n in range(len(clients_order)):
            order_dict = {
                "чат:": order_name,
                "клиент:": clients_order[n].text,
                "когда:": dates_order[n].text,
                "адрес:": addresses_order[n].text,
                "тема:": subjects_order[n].text,
                "проблема:": descriptions_order[n].text
                }
            if order_name == "-- В работе --":
                order_dict["стоимость заказа:"] = prices_order[n].text
            order_list.append(order_dict)

            problem = order_list[n]['проблема:']
            split_problem = problem.split('\n')

            problem_list = []

            for item in split_problem:
                split_item = item.split(' ')
                if 'Марка:' in split_item:
                    order_list[n]['марка:'] = split_item[1].split('.')[0] # split word from '.'
                elif 'Модель:' in split_item:
                    order_list[n]['марка:'] = order_list[n]['марка:'] + " " + split_item[1].split('.')[0] # split word from '.'
                else:
                    problem_list.append(item)

            order_list[n]['проблема:'] = ' '.join(problem_list)
            if order_list[n]['проблема:'] == []:
                order_list[n]['проблема:'] = order_list[n]['тема:']


            # search_list[n] = order_list[n]['марка:'] + " " + order_list[n]['проблема:']

    return order_list


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
        # Find out href link to enter Open Orders
        open_orders = driver.find_element(By.ID, "js-tab-orders-repls").get_attribute('href')
        # print(open_orders)
        time.sleep(5)

        # inside chat
        driver.get(url=open_orders)
        time.sleep(5)

        # Returning info from Open Orders
        return get_info("-- Открытые ордера --")
