from get_info import *

# Functions to open webpages for search
enter_web_page()
enter_chat()

# Lists to save and to work with data
working_list = []
open_list = []

# Main Program
try:
    while True:
        # ===========================================
        # Info about Working Orders
        working_temp = working_orders()
        # print(working_temp)

        # Here is printing order information in column
        display_orders(working_temp)

        # Trying to find problem in Youtube
        search_text = working_temp[0]['марка'] + " " + working_temp[0]['проблема']
        print(search_text)

        # # ===========================================
        # # Info about Open Orders
        # open_temp = open_orders()
        # # print(open_temp)
        #
        # # Here is printing order information in column
        # display_orders(open_temp)
        #
        # # Trying to find problem in Youtube
        # search_text = open_temp[0]['марка'] + " " + open_temp[0]['проблема']
        # print(search_text)

        # ===========================================

        time.sleep(120)
        print("\n\n... 2 minutes passed ...\n\n")

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
