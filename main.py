from get_info import *

# functions to open webpages for search
enter_web_page()
enter_chat()

# dictionaries to save and to work with data
working_list = []
open_list = []

# Main Program
try:
    while True:
        # ===========================================
        # Info about Working Orders
        working_temp = working_orders()

        for order in working_temp:
            if order not in working_list:
                working_list.append(order)
                print(" ... working order added to list ...")
                print(working_list)
            else:
                print(" ... working order is in a list ... ")


    # ===========================================
        # Info about Open Orders
        # open_save = open_orders()
        # ===========================================

        time.sleep(120)
        print("\n\n... 2 minutes passed ...\n\n")

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
