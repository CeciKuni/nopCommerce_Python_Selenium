from Locators.locators import LogInLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def setUsername(self, username):
        self.driver.find_element(*LogInLocators.textbox_username_id).clear()
        self.driver.find_element(*LogInLocators.textbox_username_id).send_keys(username)
        
    def setPassword(self, password):
        self.driver.find_element(*LogInLocators.textbox_password_id).clear()
        self.driver.find_element(*LogInLocators.textbox_password_id).send_keys(password)
        
    def clickLogin(self):
        self.driver.find_element(*LogInLocators.button_login_xpath).click()
        
    def clickLogout(self):
        self.driver.find_element(*LogInLocators.link_logout_linktext).click()