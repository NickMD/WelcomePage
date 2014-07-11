from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class welcomePage(object):
    def __init__(self,driver):
        self.driver = driver

    def login(self, fname, lname, email, phone, gender, state, agree=True):
        try:    #Wait until first field is element_to_be_clickable. Locator hardcoded.
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,"id_fname")))
        except:
            print "Field FirstName not found. Page not loaded in 10 seconds."
        self.driver.find_element_by_id("id_fname").send_keys(fname)
        self.driver.find_element_by_id("id_lname").send_keys(lname)
        self.driver.find_element_by_id("id_email").send_keys(email)
        self.driver.find_element_by_id("id_phone").send_keys(phone)
        if gender == "M":
            self.driver.find_element_by_id("id_g_radio_01").click()
        elif gender == "F":
            self.driver.find_element_by_id("id_g_radio_02").click()
        stateselector = "//select[@id='id_state']/option[@value='%s']" % state # Select state from parameters
        self.driver.find_element_by_xpath(stateselector).click()
        if agree:                                                      # Agree is True by default
            self.driver.find_element_by_id("id_checkbox").click()
        try:
            self.driver.find_element_by_id("id_checkbox").is_selected() == True # Just to make debug and make sure that checkbox selected.
        except:
            print "Agree checkbox broken"

        self.driver.find_element_by_id("id_submit_button").click()
        return self.driver








