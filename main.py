from get_info import *

enter_web_page()
enter_chat()

try:
    while True:
        # ===========================================
        # Info about Working Orders
        # working_orders()
        # ===========================================
        # Info about Open Orders
        # open_orders()
        # ===========================================

        saving_working_orders = working_orders()


        time.sleep(120)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
