from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Screenshot import Screenshot
from selenium.webdriver.common.alert import Alert
import time


# Handle Alerts js


class AletsDemmo:
    def alets_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')
        # driver.switch_to.frame("iframeResult")
        #
        # #accept the alert
        # driver.find_element(By.TAG_NAME, "button").click()
        # time.sleep(3)
        # text_on_alert = driver.switch_to.alert.text
        # print(text_on_alert)
        # driver.switch_to.alert.accept()
        # time.sleep(10)
        #
        # # Dismiss( cancel)  the alert
        # driver.find_element(By.TAG_NAME, "button").click()
        # time.sleep(3)
        # driver.switch_to.alert.dismiss()
        # time.sleep(10)

        #send text
        driver.get("https://www.w3schools.com/jsreF/tryit.asp?filename=tryjsref_prompt")
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(3)

        #1 old version
        # driver.switch_to.alert.send_keys("Selenium alert")
        # time.sleep(3)
        # driver.switch_to.alert.accept()

        # 2 new version
        alert = Alert(driver)
        alert.send_keys("Selenium alert")
        alert.accept()

        time.sleep(10)




"""
1. Simple Alert
2. Confirmation Alert
3. Prompt Alert

alert.accept() – Will click on OK button

alert.dismiss() – Will click on Cancel button

alert.text – will get the text which is present on the Alert
"""


get_alert = AletsDemmo()
get_alert.alets_demo()