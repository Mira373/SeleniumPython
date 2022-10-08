from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

# Calendar in Selenium


class CalendarDemo:
    def calendar_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://tkt.ge/')
        click_flights = driver.find_element(By.CLASS_NAME, 'icon-flights').click()
        time.sleep(10)


        # it is not working
        one_click = driver.find_element(By.XPATH, '//*[@id="flights-search-form"]/div[2]/div[2]').click
        time.sleep(10)
        # calendar_date = driver.find_element(By.XPATH, "//div[@class='day toMonth valid tmp'][normalize-space()='12']").click()
        # find_calendar_days = driver.find_elements(By.XPATH, "//div[@id='month-wrapper']//tbody//td[@class='day']")
        # for day in find_calendar_days:
        #     if day.get_attribute("innerHTML") == "11.10.2022":
        #         day.click()
        #         break
        #         time.sleep(10)

            # print(day.text)


calendar = CalendarDemo()
calendar.calendar_demo()

