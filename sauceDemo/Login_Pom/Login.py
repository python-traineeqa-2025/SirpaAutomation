from sauceDemo.Login_Pom.Login_prop import LoginProperties

class Login(LoginProperties):

    # Login Page
    def __init__(self, driver):
        self.driver = driver


    def login(self,Username,password):
        # self.Username=Username
        # self.password=password

        uname = self.username_input
        uname.send_keys(Username)

        pwd= self.password_input
        pwd.send_keys(password)

        loginbtn=self.login_button
        loginbtn.click()