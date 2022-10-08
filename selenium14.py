from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Screenshot import Screenshot
import time

#execute JavaScript

class Demo_Javascript:

    def javascript_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://github.com/')
        # list_elements = driver.find_element(By.CSS_SELECTOR, 'p')
        # list_elements = driver.execute_script("return document.getElementsByTagName('p')[1];")
        # driver.execute_script("arguments[1].innerText", list_elements)

        # js = 'alert("Hello Selenium")'
        # driver.execute_script(js)

        driver.execute_script("document.getElementsByClassName('btn-mktg')[0].click()")
        time.sleep(10)

demojs = Demo_Javascript()
demojs.javascript_demo()