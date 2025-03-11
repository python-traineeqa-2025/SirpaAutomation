from sauceDemo.Product_Pom.product_prop import productProperties
import logging
import time

class Product(productProperties):
    def __init__(self, driver):
        self.driver = driver

    def productdetails(self):

        title = self.productInput
        title.click()

        desc=self.Description
        d = desc.text
        logging.info(d)

        price=self.Price
        print(price.text)

        time.sleep(5)


