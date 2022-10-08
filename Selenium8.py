from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



class HiddenElementDemo:
    def show_hide_Demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")

        #1 in this case element is there in DOM

        # boolean value will be returned
        show_hide_element = driver.find_element(By.XPATH, '//*[@id="myDIV"]').is_displayed()
        print(show_hide_element)
        #when you click element disappears
        show_hide_element_click = driver.find_element(By.XPATH, '//*[@id="main"]/button').click()
        show_hide_element2 = driver.find_element(By.XPATH, '//*[@id="myDIV"]').is_displayed()
        print(show_hide_element2)
        time.sleep(10)

        # 2 in this case element is not  there in DOM


    def show_hide_Demo_2(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/hotels")
        textbox_icon= driver.find_element(By.XPATH, '//*[@id="booking_engine_modues"]/div').click()
        plus_icon = driver.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_box"]/div[1]/div[2]/div[3]/div/div/span[2]').click()
        show_hide_element_2 = driver.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_box"]/div[1]/ul/li[1]/span').is_displayed()
        print(show_hide_element_2)
        minus_icon = driver.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_box"]/div[1]/div[2]/div[3]/div/div/span[1]').click()
        show_hide_element_2_1 = driver.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_box"]/div[1]/ul/li[1]/span').is_displayed()
        print(show_hide_element_2_1)
        time.sleep(10)
#1 case
show_hide_get = HiddenElementDemo()
show_hide_get.show_hide_Demo()
#2 case
# show_hide_get_2 = HiddenElementDemo()
# show_hide_get_2.show_hide_Demo_2()