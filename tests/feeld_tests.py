import unittest
from HTMLTestRunner import HTMLTestRunner
from _lib._lib import *
from actions import Feeld_Actions
from locators import Feeld_Locators
import os
from appium import webdriver
from time import sleep
import datetime

class FeeldTests(unittest.TestCase):
    # Execute BEFORE Test Suite
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = 'sdk_gphone_x86'
        desired_caps['appPackage'] = 'co.feeld'
        desired_caps['appActivity'] = 'host.exp.exponent.Default'
        desired_caps['noReset'] = 'true'
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(20)

    # Execute BEFORE each Test
    def setUp(self):
        # Write test name into the Textbox file
        test_name = '.'.join(self._testMethodName.split('.')[-2:])
        f = open(os.path.join(os.getcwd(), 'tools', 'textbox', 'textbox.txt'), 'w')
        f.write(test_name)
        f.close()

    # Execute AFTER each test
    def tearDown(self):
        pass

    # Execute AFTER Test Suite
    @classmethod
    def tearDownClass(cls):
        #cls.driver.close()
        cls.driver.quit()
        print("Test Suite Completed")

    def test_100_update_about_info(self):
        timestamp = datetime.datetime.now().strftime('%H_%M_%S')
        about_text = str(timestamp) + " Test About input"
        Feeld_Actions.open_user(self, self.driver)
        Feeld_Actions.open_edit_profile(self, self.driver)
        Feeld_Actions.scroll_down(self, self.driver, 0, 500)

        Feeld_Actions.write_field_text(self, self.driver, Feeld_Locators.FIELD_ABOUT, about_text)
        Feeld_Actions.click_back_button(self, self.driver)

        Feeld_Actions.open_edit_profile(self, self.driver)
        Feeld_Actions.scroll_down(self, self.driver, 0, 500)

        expected_text = about_text
        actual_text = Feeld_Actions.get_field_text(self, self.driver, Feeld_Locators.FIELD_ABOUT)

        Reporting.test_log("Expected Text: " + expected_text)
        Reporting.test_log("Actual Text:   " + expected_text)
        self.assertEqual(expected_text, actual_text, "Expected text is not equal to Actual text")
        sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FeeldTests)
    runner = HTMLTestRunner(log=False, verbosity=2, output='Report_html', title='Test report', report_name='Report',
                            description="HTMLTestReport")
    runner.run(suite)
