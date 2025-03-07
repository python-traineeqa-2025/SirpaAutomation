from sys import executable
from selenium import webdriver
from selenium.webdriver.common.by import By


class Youtube():
    def home(self):
        #driver.manage().window().setSize()
        driver.get("https://www.youtube.com/")
        driver.find_element(By.NAME, 'search_query').send_keys('selenium python project')
        driver.find_element(By.CSS_SELECTOR, '.ytSearchboxComponentSearchButton').click()
        driver.find_element(By.CLASS_NAME, 'style-scope ytd-video-renderer').click()
searchpage= Youtube() #class name
searchpage.home() #function name