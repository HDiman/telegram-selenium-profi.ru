from enter_profi import *

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



# order = [{'ордер': '-- Открытые ордера --', 'клиент': 'Алексей', 'заказ от': '5 часов назад', 'адрес': 'Дмитровский (Московская область, Дмитровский городской округ, СНТ Фрегат, 79)', 'тема': 'Ремонт стиральной машины bosch maxx5', 'проблема': 'Не вращает барабан.\nМарка: Bosch.\nМодель: Maxx5.\nМашина работает полностью, но барабан перестал крутится.'}]
# order_1 = order
# print(order_1)
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
# print(order_2)
#
# # if order_2[0]['адрес'] in order_1[0].values():
# #     print(order_2[0]['адрес'])
#
# search_text = order_2[0]['проблема'] + " " + order_2[0]['марка'] + " " + order_2[0]['модель']
# # search_text = search_text.split('.')
# print(search_text)

search_text = "Bosch Maxx5 Не вращает барабан."
print(search_text)
# Link to Youtube
url = "https://www.youtube.com/"

# Opening Youtube channel
driver.get(url=url)
time.sleep(5)
print("test_1")
time.sleep(5)

# Inserting text into search
text_input = driver.find_element(By.ID, "search")
print("test_2")
time.sleep(5)

# text_input.clear()
print("test_3")
time.sleep(5)

text_input.send_keys(search_text)
print("test_4")
time.sleep(5)

driver.find_element(By.ID, "search-icon-legacy").click()
