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

        # Here is printing order information in column
        print_orders(working_temp)


        # ===========================================
        # Info about Open Orders
        open_temp = open_orders()

        # Here is printing order information in column
        print_orders(open_temp)

        # ===========================================

        time.sleep(120)
        print("\n\n... 2 minutes passed ...\n\n")

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
