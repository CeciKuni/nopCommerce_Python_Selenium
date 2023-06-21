import time
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomersPage import AddCustomer
from PageObjects.SearchEditCustomerPage import SearchCustomer
from Utilities.readProperties import ReadConfig, date_time
from Utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getAplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger
    email = ReadConfig.getEmail()


    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* Searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail(self.email)
        searchcust.clickSearch()
        time.sleep(3)
        status = searchcust.searchCustomerByEmail(self.email)
        assert True == status
        self.driver.close()
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
