from selenium.webdriver.common.by import By

from Test.conftest import params
from config.configuration import TestConfig
from utility.basepage import BasePage
from selenium.webdriver.common.keys import Keys


class Home(BasePage):
    """
    storing the locators in a variable
    """

    search_box = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    click_search_submit = (By.XPATH, "//input[@id='nav-search-submit-button']")

    def __init__(self, driver):
        self.driver = driver

    # type the items in search bar
    def search_box_meth(self, params):
        if self.is_search_box_present():
            self.driver.find_element(*Home.search_box).send_keys(params['search_item'])
            self.message_logging("search box is present")
            self.driver.find_element(*Home.search_box).send_keys(Keys.ENTER)
        else:
            self.message_logging("search box not present")

    def is_search_box_present(self):
        search_box = self.driver.find_elements(*Home.search_box)
        present = False
        if len(search_box) >= 1:
            present = True
        return present

    """click the search button"""

    def click_button(self):
        return self.driver.find_element(*Home.click_search_submit).click()
