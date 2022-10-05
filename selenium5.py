from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class GetTextDemo:
    def get_text_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://github.com/")
        text_in_p = driver.find_element(By.XPATH, "/html/body/div[4]/main/div[1]/div[1]/div[1]/div/div/div[1]/p").text
        print(text_in_p)
        time.sleep(10)
textgetting = GetTextDemo()
textgetting.get_text_demo()


