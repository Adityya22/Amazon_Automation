import time

from config.configuration import TestConfig
from Pages.itemSelected import Item_Selected
from Pages.purchase import Purchase
from utility.basepage import BasePage
from Pages.loginPage import Credential
from Pages.homePage import Home


class Test_amazon(BasePage):

    def test_search(self, params):
        """
        creating home object
        """
        home = Home(self.driver)

        # calling methods of Home class
        home.search_box_meth(params)

    def test_items(self):
        """
        creating object of ItemSelected class
        """
        items = Item_Selected(self.driver)

        # print all product list after search
        results = items.get_result()
        for result in results:
            self.message_logging(result.text)

        # switch to the fourth searched items
        items.click_second()

        # switch to new window frame
        items.frame_switch()

        # scroll down to buy now option
        items.scroll()

    def test_purchase(self):

        """
        creating object of Purchase class
        """
        buy_now = Purchase(self.driver)
        windows_opened = self.driver.window_handles
        self.driver.switch_to.window(windows_opened[1])
        buy_now.buy()

    def test_login(self, params):
        """
        creating object of Credential class
        """
        cred = Credential(self.driver)

        # type email in the login form
        cred.email_meth().send_keys(params['email'])
        cred.continue_click()
        time.sleep(2)

        # type password
        cred.pass_meth().send_keys(params['password'])
        time.sleep(2)
        cred.click_signin_meth()

        # get the message
        try:
            message = cred.get_message()
            if TestConfig.text1 in message:
                # assert (TestConfig.text1 in message)
                self.message_logging(TestConfig.text1)
            elif TestConfig.text2 in message:
                # assert (TestConfig.text2 in message)
                self.message_logging(TestConfig.text2)

        except Exception as err:
            raise err



