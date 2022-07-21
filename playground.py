# from enter_profi import *
# import json


# # From here we send printing info
# def display_orders(order):
#     for lt in range(len(order)):
#         for key, value in order[lt].items():
#             print(f"{key}: {value}")
#         print("\n")
#         time.sleep(5)


# def yes_no_open_orders(open_temp):
#     # ===========================================
#     # Info about Open Orders
#     # open_temp = open_orders()
#     if open_temp != []:
#         # Here is printing order information in column
#         # display_orders(open_temp)
#
#         # Trying to find problem in Youtube
#         search_text = open_temp[0]['марка'] + " " + open_temp[0]['модель'] + " " + open_temp[0]['проблема']
#         return search_text
#     else:
#         return "No open orders"
#
#
# def yes_no_working_orders(working_temp):
#     # ===========================================
#     # Info about Working Orders
#     # working_temp = working_orders()
#     if working_temp != []:
#         # Here is printing order information in column
#         # display_orders(working_temp)
#
#         # Trying to find problem in Youtube
#         search_text = working_temp[0]['марка'] + " " + working_temp[0]['модель'] + " " + working_temp[0]['проблема']
#         return search_text
#     else:
#         return "No working orders"


# # ===========================================
# time.sleep(120)
# print("\n\n... 2 minutes passed ...\n\n")


# for n in range(len(open_temp)):
#     for key, value in open_temp[n].items():
#         bot.send_message(message.chat.id, f"{key}: {value}")
#         print(f"{key}: {value}")


# # Functions to open webpages for search
# enter_web_page()
# enter_chat()

# # Main Program
# try:
#     while True:
#         # This function gets and print info about open and working orders
#         info_open_working_orders()
#
#
# except Exception as ex:
#     print(ex)
#
# finally:
#     driver.close()
#     driver.quit()


# From here we send printing info
# def print_orders(order):
#     for n in range(len(order)):
#         print(f"\n{order[n]['ордер']}\n"
#               f"клиент: {clients_order[n].text}\n"
#               f"заказ от: {dates_order[n].text}\n"
#               f"адрес: {addresses_order[n].text}\n"
#               f"тема: {subjects_order[n].text}\n"
#               f"проблема: {descriptions_order[n].text}")
#         if order_name == "-- В работе --":
#             print(f"стоимость заказа: {prices_order[n].text}\n")
#         time.sleep(5)

# for lt in range(len(order)):
#     for key, value in order[lt].items():
#         print(f"{key}: {value}")


# print(order)

# ордер: -- Открытые ордера --
# клиент: Ася
# заказ от: 1 час назад
# адрес: Московский (Московский, 1-й микрорайон, 23Г)
# тема: Ремонт стиральных машин indesit
# проблема: Не включается.
# марка: Indesit

# search_text = "Bosch Maxx5 Не вращает барабан."
# print(search_text)
# # Link to Youtube
# url = "https://www.youtube.com/"
#
# # Opening Youtube channel
# driver.get(url=url)
# time.sleep(5)
# print("test_1")
# time.sleep(5)
#
# # Inserting text into search
# text_input = driver.find_element(By.ID, "search")
# print("test_2")
# time.sleep(5)
#
# # text_input.clear()
# print("test_3")
# time.sleep(5)
#
# text_input.send_keys(search_text)
# print("test_4")
# time.sleep(5)
#
# driver.find_element(By.ID, "search-icon-legacy").click()

# str_line = ''
# for item in order_3:
#     tpl = " ".join(item)
#     str_line = str_line + tpl + '\n'
#
# print(str_line)


# order = [{'ордер': '-- Открытые ордера --', 'клиент': 'Алексей', 'заказ от': '5 часов назад', 'адрес': 'Дмитровский (Московская область, Дмитровский городской округ, СНТ Фрегат, 79)', 'тема': 'Ремонт стиральной машины bosch maxx5', 'проблема': 'Не вращает барабан.\nМарка: Bosch.\nМодель: Maxx5.\nМашина работает полностью, но барабан перестал крутится.'}]
# order_1 = order
# # print(order_1)
#
# problem = order[0]['проблема']
# split_problem = problem.split('\n')
#
# problem_list = []
# for item in split_problem:
#     split_item = item.split(' ')
#     if 'Марка:' in split_item:
#         order[0]['марка'] = split_item[1].split('.')[0] # split word from '.'
#     elif 'Модель:' in split_item:
#         order[0]['модель'] = split_item[1].split('.')[0] # split word from '.'
#     else:
#         problem_list.append(item)
#
# order[0]['проблема'] = ' '.join(problem_list)
# order_2 = order
#
# # print(order_2)
#
# # if order_2[0]['адрес'] in order_1[0].values():
# #     print(order_2[0]['адрес'])
#
# def two_items():
#     search_text = order_2[0]['проблема'] + " " + order_2[0]['марка'] + " " + order_2[0]['модель']
#     # search_text = search_text.split('.')
#     print(search_text)
#
#     order_3 = list(order_2[0].items())
#     # order_4 = " ".join(order_3)
#     print(order_3)
#     return order_3, search_text
#
# two = two_items()
#
# print(two)
# print(two[0])
# print(two[1])

model = "модель: Maxx 5."
print(model)

model_2 = model.split(" ")
model_3 = ""
for i in range(len(model_2)):
    if model_2[i] == 'модель:':
        pass
    else:
        model_3 = model_3 + " " + model_2[i]
model_3 = model_3.split('.')[0]
print(model_3)
