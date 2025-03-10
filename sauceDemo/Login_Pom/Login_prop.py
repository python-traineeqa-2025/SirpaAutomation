from sauceDemo.Login_Pom.Login_Locator import LoginLocators

class LoginProperties(LoginLocators):

    @property
    def username_input(self):
        return self.driver.find_element(*LoginLocators.Username)

    @property
    def password_input(self):
        # self.wait=WebDriverWait(self.driver,20)
        # self.wait.until()
        return self.driver.find_element(*LoginLocators.password)

    @property
    def login_button(self):
        return self.driver.find_element(*LoginLocators.login_btn)