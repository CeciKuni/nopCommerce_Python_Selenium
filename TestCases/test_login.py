import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig, date_time
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getAplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("************** Test_001_Login ****************")
        self.logger.info("************** Verifying Home Page Title ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("************** Verifying Home Page Title - Passed ****************")
            self.driver.close()
            assert True
        else:
            self.logger.error("************** Verifying Home Page Title - Failed ****************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle_Fail_" + date_time + ".png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************** Verifying Login Test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)   
        self.lp.setPassword(self.password)    
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("************** Verifying Login Test - Passed ****************")
            assert True
        else:
            self.logger.error("************** Verifying Login Test - Failed ****************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_Fail_" + date_time + ".png")
            assert False
        self.driver.close()