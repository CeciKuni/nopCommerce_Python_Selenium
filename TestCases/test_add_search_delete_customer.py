from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomersPage import AddCustomer
from PageObjects.SearchEditCustomerPage import SearchCustomer
from Utilities.readProperties import ReadConfig, date_time
from Utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
import string
import random
import time
import pytest


class Test_003_Add_Search_Delete_Customer:
    baseURL = ReadConfig.getAplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger


    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size)) + "@gmail.com"

    email = random_generator()

    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Armando")
        self.addcust.setLastName("Barreda")
        self.addcust.setDob("7/05/1985")  # Format: D / MM / YYY
        self.addcust.setCompanyName("CK")
        self.addcust.setAdminComment("This is for testing.........")
        self.addcust.clickOnSave()
        time.sleep(5)

        self.logger.info("************* Saving customer info, email: %s ************************", self.email)

        self.logger.info("********* Add customer validation started *****************")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add Customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_Fail_" + date_time + ".png")
            self.logger.error("********* Add Customer Test Failed ************")
            assert False
        self.logger.info("******* Ending Add Customer Test **********")

        # Searching the email added before
        self.logger.info("******* Searching the email: %s **********", self.email)
        self.searchCust = SearchCustomer(self.driver)
        self.searchCust.setEmail(self.email)
        self.searchCust.searchCustomerByEmail(self.email)
        self.searchCust.clickSearch()
        self.logger.info("***************  Searching Customer Finished  *********** ")

        # Pressing button Edit
        self.searchCust.editCustomer()
        self.searchCust.deleteCustomer()
        self.searchCust.confirmDeleteCustomer()
        self.logger.info("********* Customer delete validation started *****************")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'The customer has been deleted successfully.' in self.msg:
            assert True
            self.logger.info("********* Add Customer Test Passed *********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_deleteCustomer_Fail_" + date_time + ".png")
            self.logger.error("********* Delete customer Test Failed ************")
            self.driver.close()
            assert False
        self.logger.info("******* Ending Delete Customer test **********")

