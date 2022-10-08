from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

#dropdown
class DropdownDemo:
    def dropdown_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.jobs.ge/")
        # dropdown_button = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div[2]/div[1]/select').click()
        dropdown_button = driver.find_element(By.NAME, 'cid')
        select = Select(dropdown_button)
        driver.maximize_window()
        option_index = select.select_by_index(3)
        time.sleep(10)
        # option_text = select.select_by_visible_text('IT/პროგრამირება')
        # time.sleep(10)
        # option_value = select.select_by_value('4')
        # time.sleep(10)

object_dropdown = DropdownDemo()
object_dropdown.dropdown_demo()