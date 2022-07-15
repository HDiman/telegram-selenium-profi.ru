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

        for order in working_temp:
            if order not in working_list:
                working_list.append(order)
                print(" ... new working order added to list ...")
            else:
                print(" ... no new one ... ")
        # print(working_list)

        # Here is printing order information in column
        print_orders(working_list)

        # ===========================================
        # Info about Open Orders
        open_temp = open_orders()

        for order in open_temp:
            if order not in open_list:
                open_list.append(order)
                print(" ... new open order added to list ...")
            else:
                print(" ... no new one ... ")
        # print(open_list)

        # Here is printing order information in column
        print_orders(open_list)

        # ===========================================

        time.sleep(120)
        print("\n\n... 2 minutes passed ...\n\n")

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
