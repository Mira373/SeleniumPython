from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Screenshot import Screenshot
import time

# Multiple Windows


class Demo_Javascript:

    def javascript_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://meama.business/')

        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[3]/div/div[2]/div[4]/div/div/a/img').click()
        time.sleep(10)

        all_handlers = driver.window_handles
        size = len(all_handlers)
        print(all_handlers)
        
    #1st option
        # for handler in all_handlers:
        #     if handler != parent_handle:
        #         driver.switch_to.window(handler)
        #         driver.find_element(By.XPATH, '//*[@id="masthead"]/div/div[4]/ul/li[2]/div/a').click()
        #         time.sleep(10)
        #         driver.close()
        #         time.sleep(5)
        #         break


        # driver.switch_to.window(parent_handle)
        # driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[3]/div/div[2]/div[4]/div/div/a/img').click()
    # 2nd option
        for i in range(size):
            if all_handlers[i] != parent_handle:
                driver.switch_to.window(all_handlers[i])
                driver.find_element(By.XPATH, '//*[@id="masthead"]/div/div[4]/ul/li[2]/div/a').click()
                time.sleep(10)
                print(driver.title)
                driver.close()
                break



        # driver.switch_to.window(parent_handle)

demojs = Demo_Javascript()
demojs.javascript_demo()