from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Screenshot import Screenshot
import time


#Capture Screenshot
#need  pip install Selenium-Screenshot

class ScreenshotDemo:
    def screenshot_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://tkt.ge/')

        click_flights = driver.find_element(By.CLASS_NAME, 'icon-flights')
        click_flights.screenshot(".//tphoto.png")
        click_flights.click()
        time.sleep(10)
        # driver.save_screenshot()
        driver.get_screenshot_as_file("C://Users//acer//Downloads//tphoto.png")



photo = ScreenshotDemo()
photo.screenshot_demo()