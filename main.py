from get_info import *

# functions to open webpages for search
enter_web_page()
enter_chat()

# dictionaries to save and to work with data
working_dict = {}
open_dict = {}

# Main Program
try:
    while True:
        # ===========================================
        # Info about Working Orders
        working_temp = working_orders()

        if working_temp['адрес:'] not in working_dict.values():
            working_dict = working_temp
            print("working order added to dictionary")
            print(working_dict)
        else:
            print(" ... working order is in dictionary ... ")

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
