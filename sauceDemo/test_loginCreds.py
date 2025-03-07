import time
import json
from setup.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginCreds(BaseTest):

    def testLoginPage(self):
        self.driver.get("https://www.saucedemo.com/")
        print("Page title:",self.driver.title)

                                            #Login Page
        users = self.creds['users']

        for uname,password in users.items():

            Username = self.driver.find_element(By.ID, 'user-name')
            Username.clear()
            Username.send_keys(uname)  #esle keys haru print garyo
            print(uname)

            pw=self.driver.find_element(By.ID,'password')
            pw.clear()
            pw.send_keys(password)
            print(password)


            login = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
            )
            login.click()


            time.sleep(5)
            self.driver.back()