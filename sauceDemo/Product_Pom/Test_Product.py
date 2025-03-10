import unittest
import logging
from setup.BaseTest import BaseTest
from sauceDemo.Product_Pom.Product import Product
from sauceDemo.Login_Pom.Login import Login

class TestProduct(BaseTest, unittest.TestCase):

    def test_product(self):
        url = self.creds["base_url"]
        self.driver.get(url)

        logging.info("Opened the site")

        login_page = Login(self.driver)

        logging.info("Getting the credentials")

        uname = self.creds["standard_username"]
        password = self.creds["Password_for_all_users"]

        logging.info("Got the credentials, now logging in")

        login_page.login(uname, password)

        pd = Product(self.driver)

        pd.productdetails()

