import time
from Locators.locators import SearchCustomerLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class SearchCustomer():
    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(*SearchCustomerLocators.txtEmail_id).clear()
        self.driver.find_element(*SearchCustomerLocators.txtEmail_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(*SearchCustomerLocators.txtFirstName_id).clear()
        self.driver.find_element(*SearchCustomerLocators.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(*SearchCustomerLocators.txtLastName_id).clear()
        self.driver.find_element(*SearchCustomerLocators.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(*SearchCustomerLocators.txtEmail_id)

    def getNoOfRows(self):
        return len(self.driver.find_elements(*SearchCustomerLocators.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(*SearchCustomerLocators.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        self.driver.find_element(*SearchCustomerLocators.btnDeleteDefaultRole_xpath).click()
        time.sleep(3)
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(*SearchCustomerLocators.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        self.driver.find_element(*SearchCustomerLocators.btnDeleteDefaultRole_xpath).click()
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(*SearchCustomerLocators.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag

    def editCustomer(self):
        btnEdit = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(*SearchCustomerLocators.btnEdit_xpath))
        )
        btnEdit.click()

    def deleteCustomer(self):
        btnDelete = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(*SearchCustomerLocators.btnDelete_xpath))
        )
        btnDelete.click()

    def confirmDeleteCustomer(self):
        modal = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(*SearchCustomerLocators.btnModalDelete_xpath))
        )
        modal.click()





