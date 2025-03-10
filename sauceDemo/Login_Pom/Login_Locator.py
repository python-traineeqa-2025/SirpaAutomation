from selenium.webdriver.common.by import By


class LoginLocators(object):
    Username =(By.ID, "user-name")
    password =(By.ID,"password")
    login_btn=(By.ID, "login-button")