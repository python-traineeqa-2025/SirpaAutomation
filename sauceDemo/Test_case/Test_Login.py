import time
from setup.BaseTest import BaseTest
from sauceDemo.Login_Pom.Login import Login

class TestLoginCreds(BaseTest):

    def test_Login(self):
        url=self.creds["base_url"]
        self.driver.get(url)
        print("Page title:",self.driver.title)

                                        #Login Page
        lg = Login(self.driver)

        Username = self.creds["standard_username"]
        password= self.creds["Password_for_all_users"]

        lg.login(Username, password)

        time.sleep(2)

