from get_info import *
import telebot
from auth_data import token


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Работаем")
        # Functions to open webpages for search
        enter_web_page()

    @bot.message_handler(content_types=['text'])
    def send_text(message):

        if message.text.lower() != 'o':
            bot.send_message(message.chat.id, "Код принят")
            enter_code(message.text)
            enter_chat()

        elif message.text.lower() == 'o':
            try:
                # OPEN ORDERS Section
                open_temp = open_orders()
                if open_temp == []:
                    bot.send_message(message.chat.id, "-- Нет ордеров: -- ОТКРЫТЫЕ --")
                    print("-- Нет ордеров: -- ОТКРЫТЫЕ --")
                else:
                    search_open = []
                    for n in range(len(open_temp)):
                        search_open[n] = open_temp[n]['марка:'] + " " + open_temp[n]['проблема:']
                        open_temp_2 = list(open_temp[n].items())
                        open_temp_3 = ''
                        for item in open_temp_2:
                            tpl = " ".join(item)
                            open_temp_3 = open_temp_3 + tpl + '\n'

                        # Printing info about order in one message
                        bot.send_message(message.chat.id, f"{open_temp_3}")
                        print(open_temp_3)

                        # Text for searching in youtube
                        bot.send_message(message.chat.id, f"{search_open[n]}")
                        print(search_open[n])

                # WORKING ORDERS Section
                working_temp = working_orders()
                if working_temp == []:
                    bot.send_message(message.chat.id, "-- Нет ордеров: -- В РАБОТЕ --")
                    print("-- Нет ордеров: -- В РАБОТЕ --")
                else:
                    search_working = []
                    for n in range(len(working_temp)):
                        search_working[n] = working_temp[n]['марка:'] + " " + working_temp[n]['проблема:']
                        working_temp_2 = list(working_temp[n].items())
                        working_temp_3 = ''
                        for item in working_temp_2:
                            tpl = " ".join(item)
                            working_temp_3 = working_temp_3 + tpl + '\n'

                        # Printing info about order in one message
                        bot.send_message(message.chat.id, f"{working_temp_3}")
                        print(working_temp_3)

                        # Text for searching in youtube
                        bot.send_message(message.chat.id, f"{search_working[n]}")
                        print(search_working[n])

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error!")
        else:
            bot.send_message(message.chat.id, "I like myself!")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(60)


if __name__ == "__main__":
    telegram_bot(token=token)
