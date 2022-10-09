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


#  Mouse Hover


class DemoMouseActions:
    def mouse_actions(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://github.com/')
        driver.maximize_window()
        nav_button = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[2]/div/nav/ul/li[3]/button")
        actions = ActionChains(driver)
        actions.move_to_element(nav_button).perform()
        # actions.move_to_element(nav_button).double_click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/ul[3]/li[2]/a").click()
        time.sleep(10)

"""

"""

demo_mouse_actions = DemoMouseActions()
demo_mouse_actions.mouse_actions()