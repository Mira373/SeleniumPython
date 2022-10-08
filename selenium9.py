from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


#checkbox radiobutton
class CheckboxRadioDemo:
    def checkbox_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://shop.meama.ge/ka")
        menu_bar = driver.find_element(By.XPATH, '//*[@id="header-bottom"]/div[2]/div[2]/ul/li[4]/a').click()
        driver.maximize_window()
        check_box = driver.find_element(By.XPATH, '//*[@id="catalog-flter"]/div[2]/div/div/label[1]/span').click()
        print(check_box)
        #verify if checkbox has been selected, it will return boolean value
        verify_check = driver.find_element(By.XPATH, '//*[@id="catalog-flter"]/div[2]/div/div/label[1]/span').is_selected()
        print(verify_check)
        time.sleep(10)

    def radiobutton_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.tbcbank.ge/web/ka")
        menu_bar = driver.find_element(By.CLASS_NAME, 'ib-login').click()
        driver.maximize_window()
        time.sleep(3)
        #false
        print(driver.find_element(By.XPATH, '//*[@id="_login_WAR_tbcpwloginportlet_loginForm"]/label[2]').is_selected())
        #get cliked
        radio_button = driver.find_element(By.XPATH, '//*[@id="_login_WAR_tbcpwloginportlet_loginForm"]/label[2]').click()

        time.sleep(15)



# get_checkbox= CheckboxRadioDemo()
# get_checkbox.checkbox_demo()

get_radiobutton = CheckboxRadioDemo()
get_radiobutton.radiobutton_demo()
