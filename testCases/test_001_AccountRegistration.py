import os
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("*** test_001_AccountRegister TestCase Started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching Application")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp = HomePage(self.driver)
        self.regpage = AccountRegistrationPage(self.driver)
        self.logger.info("Clicking on My Account Element ==> Register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("Proving customer details for registration")
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = randomString.random_string_generator()+"@gmail.com"
        # self.email = ReadConfig.getUseremail()
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("546578")
        self.regpage.setPassword(ReadConfig.getPassword())
        self.regpage.setConfirmPassword(ReadConfig.getPassword())
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Acoount Registration is Passed")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
            self.logger.info("Acoount Registration is Failed")
            self.driver.close()
            assert False
        self.logger.info("**** test_001_AccountRegistration finished *** ")