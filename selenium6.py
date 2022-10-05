from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class ArttributeValueDemo:
    def get_attributeValue_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://github.com/")
        # attributes are  class, name, value, type, ...
        valueOfAttribute = driver.find_element(By.XPATH, "/html/body/div[4]/main/div[1]/div[1]/div[1]/div/div/div[1]/form/div/button").get_attribute("class")
        print(valueOfAttribute)
        time.sleep(10)
attributevalueget = ArttributeValueDemo()
attributevalueget.get_attributeValue_demo()