from Locators.locators import AddCustomersLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AddCustomer:
    def __init__(self, driver):
        self.driver = driver
    def clickOnCustomersMenu(self):
        self.driver.find_element(*AddCustomersLocators.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        ele = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(*AddCustomersLocators.lnkCustomers_menuItem_xpath))
        )
        ele.click()

    def clickOnAddnew(self):
        btn_save = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(*AddCustomersLocators.btnAddNew_xpath))
        )
        btn_save.click()

    def setEmail(self, email):
        self.driver.find_element(*AddCustomersLocators.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(*AddCustomersLocators.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(*AddCustomersLocators.lbCustomersRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(*AddCustomersLocators.lstItemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(*AddCustomersLocators.lstItemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(*AddCustomersLocators.btDeleteCustomerRole_xpath).click()
            self.listitem = self.driver.find_element(*AddCustomersLocators.lstItemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(*AddCustomersLocators.lstItemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(*AddCustomersLocators.lstItemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(*AddCustomersLocators.lstItemRegistered_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(*AddCustomersLocators.lbManagerOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(*AddCustomersLocators.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(*AddCustomersLocators.rdFemaleGender_id).click()
        else:
            self.driver.find_element(*AddCustomersLocators.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(*AddCustomersLocators.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(*AddCustomersLocators.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(*AddCustomersLocators.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(*AddCustomersLocators.txtCompanyName_xpath).send_keys(comname)

    def setAdminComment(self, content):
        self.driver.find_element(*AddCustomersLocators.txtComment_id).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(*AddCustomersLocators.btnSave_xpath).click()
