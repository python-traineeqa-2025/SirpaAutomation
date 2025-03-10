from sauceDemo.Product_Pom.product_prop import productProperties
import logging

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




