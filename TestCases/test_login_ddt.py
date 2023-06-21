import time
from selenium import webdriver
import pytest
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadConfig, date_time
from Utilities.customLogger import LogGen
from Utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getAplicationURL()
    path = ".//TestData//LoginData.xlsx"
    sheetName = "Hoja1"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("************** Test_002_DDT_Login ****************")
        self.logger.info("************** Verifying Login DDT ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, self.sheetName)
        print("Number of Rows: ", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, self.sheetName, r, 1)
            self.password = XLUtils.readData(self.path, self.sheetName, r, 2)
            self.exp = XLUtils.readData(self.path, self.sheetName, r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Passed*****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*****Failed*****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Failed*****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*****Passed*****")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("**********Login DDT test Passed**********")
            self.driver.close()
            assert True
        else:
            self.logger.info("**********Login DDT test Failed**********")
            self.driver.close()
            assert False

        self.logger.info("**********End of Login DDT**********")
        self.logger.info("**********Completed TC_LoginDDT_002**********")

