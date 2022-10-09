from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Screenshot import Screenshot
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time


#Perform Drag and Drop

class DemoDragDrop:
    def drag_drop(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_draganddrop')
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        element_drag = driver.find_element(By.ID, 'drag1')
        element_drop = driver.find_element(By.ID, 'div1')
        ActionChains(driver).drag_and_drop(element_drag, element_drop).perform()
        time.sleep(20)

"""
-----
"""

item_move = DemoDragDrop()
item_move.drag_drop()