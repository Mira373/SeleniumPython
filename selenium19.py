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

#handle Sliders

class DemoSliders:
    def sliders_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://alta.ge/phones-and-communications/smart-watch-accessories.html?features_hash=17-9-559-USD')
        driver.maximize_window()
        element1 = driver.find_element(By.XPATH,"//body/div[@id='tygh_container']/div[@id='tygh_main_container']/div[contains(@class,'tygh-content clearfix')]/div[contains(@class,'category-grid inner-cg')]/div[contains(@class,'row-fluid')]/div[contains(@class,'span4')]/div[contains(@class,'sidebox-filters')]/div[@id='sidebox_27']/div[@id='product_filters_27']/div[contains(@class,'ty-product-filters__wrapper')]/div[contains(@class,'ty-product-filters__block')]/div[@id='content_27_17']/div[@id='slider_27_17']/span[1]")
        driver.find_element(By.XPATH, '//*[@id="slider_27_17"]/span[2]')
        # 1st version
        ActionChains(driver).drag_and_drop_by_offset(element1, 60, 0).perform()
        # 2nd version
        ActionChains(driver).click_and_hold(element1).pause(1).move_by_offset(60,0).release().perform()
        # 3rd version
        ActionChains(driver).move_to_element(element1).pause(1).click_and_hold(element1).move_by_offset(60,0).release().perform()
        time.sleep(10)

"""
go back ,  indicate -60
"""

modify_slider =DemoSliders()
modify_slider.sliders_demo()
