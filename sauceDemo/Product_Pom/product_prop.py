from sauceDemo.Product_Pom.product_Locators import productLocators

class productProperties(productLocators):

    @property
    def productInput(self):
        return self.driver.find_element(*productLocators.ptitle)

    @property
    def Description(self):
        Desc= self.driver.find_element(*productLocators.desc)
        return Desc

    @property
    def Price(self):
        Price=self.driver.find_element(*productLocators.price)
        return Price

