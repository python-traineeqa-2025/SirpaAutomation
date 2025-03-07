
from sys import executable

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class login():
    def loginpage(self):
        options= webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        driver=webdriver.Chrome(options=options)

        driver.get("https://foodmandu.com")
        # driver.find_element(By.NAME,'Email').send_keys('example@gmail.com')
        # driver.find_element(By.NAME,'Password').send_keys('12345678')
        # driver.find_element(By.CSS_SELECTOR, 'input[type=\"checkbox\"] + label').click()
        # driver.find_element(By.CSS_SELECTOR, '.btn-block').click()
        driver.find_element(By.CSS_SELECTOR, '.input-group .form-control:not(:last-child), .input-group-addon:not(:last-child), .input-group-btn:not(:last-child) > .btn, .input-group-btn:not(:last-child) > .btn-group > .btn, .input-group-btn:not(:last-child) > .dropdown-toggle, .input-group-btn:not(:first-child) > .btn:not(:last-child):not(.dropdown-toggle), .input-group-btn:not(:first-child) > .btn-group:not(:last-child) > .btn').send_keys('Korean')
        driver.find_element(By.CSS_SELECTOR, '.hero__container button.btn').click()



findbyname= login()
findbyname.loginpage()