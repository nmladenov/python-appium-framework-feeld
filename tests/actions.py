from time import sleep
from _lib._lib import Reporting

from locators import Feeld_Locators

class Feeld_Actions(object):
    def __init__(self, driver):
        self.driver = driver

    def open_user(self, driver):
        Reporting.test_log("Open User Tab")
        tab_user = self.driver.find_element_by_xpath(Feeld_Locators.TAB_USER)
        tab_user.click()
        sleep(3)

    def open_edit_profile(self, driver):
        Reporting.test_log("Open Edit Profile")
        button_edit_profile = self.driver.find_element_by_xpath(Feeld_Locators.BUTTON_EDIT_PROFILE)
        button_edit_profile.click()
        sleep(3)

    def scroll_down(self, driver, x, y):
        x_init = 450
        y_init = 1500
        x_end = x_init - x
        y_end = y_init - y
        Reporting.test_log("Scroll Down")
        self.driver.swipe(x_init, y_init, x_end, y_end, 1000)
        sleep(1)
        self.driver.swipe(x_init, y_init, x_end, y_end, 1000)
        sleep(3)

    def scroll_up(self, driver, x, y):
        x_init = 450
        y_init = 500
        x_end = x_init + x
        y_end = y_init + y
        Reporting.test_log("Scroll Up")
        self.driver.swipe(x_init, y_init, x_end, y_end, 1000)
        sleep(1)
        self.driver.swipe(x_init, y_init, x_end, y_end, 1000)
        sleep(3)

    def write_field_text(self, driver, field_locator, text):
        Reporting.test_log("Write Text in Field ")
        field_text = self.driver.find_element_by_xpath(field_locator)
        field_text.clear()
        field_text.send_keys(text)
        sleep(3)

    def get_field_text(self, driver, field_locator):
        Reporting.test_log("Get Text from Field")
        field_text = self.driver.find_element_by_xpath(field_locator)
        Reporting.test_log("Text from Field: " + field_text.text)
        return field_text.text

    def click_back_button(self, driver):
        Reporting.test_log("Click Back Button")
        button_back = self.driver.find_element_by_xpath(Feeld_Locators.BUTTON_BACK)
        button_back.click()
        sleep(3)

