from get_info import *
import telebot
from auth_data import token


# Functions to open webpages for search
enter_web_page()
enter_chat()

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


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Работаем")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'o':
            try:
                open_temp = open_orders()
                open_reply = yes_no_open_orders(open_temp)
                bot.send_message(message.chat.id, f"{open_reply}")
                print(open_reply)

                if open_reply != "No open orders":
                    for lt in range(len(open_temp)):
                        for key, value in open_temp[lt].items():
                            bot.send_message(message.chat.id, f"{key}: {value}")
                            print(f"{key}: {value}")
                        time.sleep(5)


                working_temp = working_orders()
                working_reply = yes_no_working_orders(working_temp)
                bot.send_message(message.chat.id, f"{working_reply}")
                print(working_reply)

                if working_reply != "No working orders":
                    for lt in range(len(working_temp)):
                        for key, value in working_temp[lt].items():
                            bot.send_message(message.chat.id, f"{key}: {value}")
                            print(f"{key}: {value}")
                        time.sleep(5)


            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error!!!")
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
