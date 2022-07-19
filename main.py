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
                open_temp = open_orders()
                if open_temp == []:
                    bot.send_message(message.chat.id, "-- Нет ордеров: -- ОТКРЫТЫЕ --")
                    print("-- Нет ордеров: -- ОТКРЫТЫЕ --")
                else:
                    for n in range(len(open_temp)):
                        open_temp_2 = list(open_temp[n].items())
                        open_temp_3 = ''
                        for item in open_temp_2:
                            tpl = " ".join(item)
                            open_temp_3 = open_temp_3 + tpl + '\n'

                        bot.send_message(message.chat.id, f"{open_temp_3}")
                        print(open_temp_3)



                working_temp = working_orders()
                if working_temp == []:
                    bot.send_message(message.chat.id, "-- Нет ордеров: -- В РАБОТЕ --")
                    print("-- Нет ордеров: -- В РАБОТЕ --")
                else:
                    pass
                    # for n in range(len(working_temp)):
                    #     for key, value in working_temp[n].items():
                    #         bot.send_message(message.chat.id, f"{key}: {value}")
                    #         print(f"{key}: {value}")

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
