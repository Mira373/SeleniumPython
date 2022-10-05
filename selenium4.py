from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class BrowserMethods:
    def demo_broswer_methods(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://github.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.minimize_window()
        driver.fullscreen_window()
        driver.find_element(By.LINK_TEXT, "Automate").click()
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.back()
        time.sleep(10)
        driver.quit()
        # driver.close()

methodsDemo = BrowserMethods()
methodsDemo.demo_broswer_methods()