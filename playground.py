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


order = [{'ордер': '-- Открытые ордера --', 'клиент': 'Алексей', 'заказ от': '5 часов назад', 'адрес': 'Дмитровский (Московская область, Дмитровский городской округ, СНТ Фрегат, 79)', 'тема': 'Ремонт стиральной машины bosch maxx5', 'проблема': 'Не вращает барабан.\nМарка: Bosch.\nМодель: Maxx5.\nМашина работает полностью, но барабан перестал крутится.'}]

# print(order)

problem = order[0]['проблема']
split_problem = problem.split('\n')

problem_list = []
for item in split_problem:
    split_item = item.split(' ')
    if 'Марка:' in split_item:
        order[0]['марка'] = split_item[1].split('.')[0] # split word from '.'
    elif 'Модель:' in split_item:
        order[0]['модель'] = split_item[1].split('.')[0] # split word from '.'
    else:
        problem_list.append(item)

order[0]['проблема'] = ' '.join(problem_list)

print(order)

for lt in range(len(order)):
    for key, value in order[lt].items():
        print(f"{key}: {value}")


