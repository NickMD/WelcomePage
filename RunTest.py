__author__ = 'NikePC'
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
from WelcomePage import welcomePage
#from selenium.webdriver.common.by import By

#from selenium.webdriver.support import expected_conditions as EC



class Test(unittest.TestCase):

#============================== Data for TC=============================================
    title_sign_up_expected = "Welcome to Sign Up"
    title_facebook_expected = "Welcome to Facebook - Log In, Sign Up or Learn More"
    error_fname_empty_expected = "Please enter First Name"
    valid_fname = "Alex"
    valid_lname = "Moore"
    valid_email = "alexmoore@gmail.com"
    valid_phone = "415 555-1212"
    errorExpectedNoFirstNAME = "Please enter First Name"
    expectedTitle = "Conformation"
    stateCA = "California"
    genderM = "M"
    genderF = "F"
    agree = "Agree"
#===================================== END =============================================

#=============================Some locators=============================================
    errorline = "ErrorLine"
    id_quotes = "id_quotes"
#===================================== END =============================================

#=============================States goes here=============================================
    california = "California"
#===================================== END =============================================


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://learn2test.net/qa/apps/sign_up/v1/")

    def testVerifyUserCanSignUp(self):
        """
        Verify that user can signup with all valid data
        """
        wait = WebDriverWait(self.driver, 10)  # Wait 10 second for element present
        wait.until(lambda driver: driver.find_elements_by_id("id_fname"))
        welcome = welcomePage(self.driver)
        welcome.login(self.valid_fname,self.valid_lname,self.valid_email,self.valid_phone,self.genderM,self.california)
        assert self.driver.title in self.expectedTitle
        self.driver.close()

    def testVerifyFirstNameRequired(self):
        """
        Verify that first name is required field and expected message displayed after form submitted with empty.
        """
        welcome = welcomePage(self.driver)
        welcome.login("", self.valid_lname, self.valid_email, self.valid_phone, self.genderM,self.california)
        assert self.errorExpectedNoFirstNAME in self.driver.find_element_by_id(self.errorline).text
        self.driver.close()

    def testQuoteDynamicCheck(self):
        """
        TC-01.03
        Verify that after refresh new quote is displayed
        """
        quootetext1 = self.driver.find_element_by_id(self.id_quotes).text
        self.driver.refresh()
        quootetext2 = self.driver.find_element_by_id(self.id_quotes).text
        self.assertNotEqual(quootetext1, quootetext2)

    def testPageContainsImageLinks(self):
        """
        TC-01.08
        Verify page contains 4 image links (Facebook, Twitter, Flickr, YouTube) all redirect to valid sites.
        """
        self.driver.find_element_by_id("id_img_facebook").click()       #Check Facebook link
        self.driver.switch_to_window(self.driver.window_handles[1])
        facebooktitle = self.driver.title
        self.assertIn("Welcome to Facebook",facebooktitle)
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

        self.driver.find_element_by_id("id_img_twitter").click()        #Check Twitter link
        self.driver.switch_to_window(self.driver.window_handles[1])
        twittertitle = self.driver.title
        self.assertIn("Twitter",twittertitle)
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

        self.driver.find_element_by_id("id_img_flickr").click()         #Check Flick link
        self.driver.switch_to_window(self.driver.window_handles[1])
        flickrtitle = self.driver.title
        self.assertIn("Flickr",flickrtitle)
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

        self.driver.find_element_by_id("id_link_youtube").click()       #Check Youtube link
        self.driver.switch_to_window(self.driver.window_handles[1])
        youtubetitle = self.driver.title
        self.assertIn("YouTube",youtubetitle)
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])


    def testIsPresentDayInFooter(self):
        """
        TC-01.10
        Verify that  data stamp in footer is actually present day, month and year.
        """
        i = datetime.datetime.now()   # Create instance for date (http://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/)
        siteDay = self.driver.find_element_by_id("timestamp").text
        realDay = ("%s %s, %s" % (time.strftime("%B"), i.day, i.year))
        self.assertIn(realDay,siteDay)







 #   def tearDown(self):
 #       pass
      #  self.driver.close()
