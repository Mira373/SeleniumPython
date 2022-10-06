from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
class FindElementByIdDemo():
    def demo_form_automation(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://github.com/")
        driver.find_element(By.LINK_TEXT, "Sign in").click()
        username_box = driver.find_element(By.ID, 'login_field')
        username_box.send_keys("usenameJD")
        password_box = driver.find_element(By.ID, 'password')
        password_box.send_keys("password123")
        enter_box = driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[11]')
        enter_box.click()
        time.sleep(20)
findById = FindElementByIdDemo()
findById.demo_form_automation()





