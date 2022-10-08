from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

#Auto Suggestion

class AutoCompletionDemo:
    def auto_completion_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://www.google.com/')
        search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search_bar.click()
        search_bar.send_keys('ილია ჭავჭავაძე')
        time.sleep(10)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(10)

         ## in the autosuggestion list , there might be limit (test case)
        # it is not working
        element_list = driver.find_elements(By.XPATH, "//ul[@role='listbox']//div[@role='presentation']//ul/li")
        print(len(element_list))
        time.sleep(10)

        # element_list = driver.find_elements(By.TAG_NAME, 'li')
        # for li in element_list:
        #     text = li.text
        #     print(text)



        # in the autosuggestion list , there might be limit (test case)

get_aut_complition = AutoCompletionDemo()
get_aut_complition.auto_completion_demo()