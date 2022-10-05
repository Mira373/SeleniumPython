from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class FindElementsByIdDemo:
    def demo_form_automation(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://github.com/")
        list_of_input = driver.find_elements(By.TAG_NAME, "a")
        print(len(list_of_input))
        for i in list_of_input:
            print(i.text)
        time.sleep(20)


findById = FindElementsByIdDemo()


findById.demo_form_automation()
