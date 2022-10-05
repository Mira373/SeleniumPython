from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



class StateOfWebelementDemo:
    def get_state_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://github.com/")
        # boolean vlue will be returned
        state_of_element = driver.find_element(By.XPATH, "/html/body/div[4]/main/div[1]/div[1]/div[1]/div/div/div[1]/form/div/button").is_enabled()
        print(state_of_element)
        time.sleep(10)
attributevalueget = StateOfWebelementDemo()
attributevalueget.get_state_demo()