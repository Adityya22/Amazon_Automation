from selenium.webdriver.common.by import By
from utility.basepage import BasePage


class Credential(BasePage):

    """
    storing the locators in a variable
    """

    email = (By.XPATH, "//input[@id='ap_email']")
    password = (By.XPATH, "//input[@id='ap_password']")
    click_continue = (By.XPATH, "//input[@id='continue']")
    click_sign_in = (By.XPATH, "//input[@id='signInSubmit']")
    message = (By.XPATH, "(//span[@class='a-list-item'])[1]")

    def __init__(self, driver):
        self.driver = driver

    # add the email-id
    def email_meth(self):
        return self.driver.find_element(*Credential.email)

    # click to continue button
    def continue_click(self):
        return self.driver.find_element(*Credential.click_continue).click()

    # add the password
    def pass_meth(self):
        return self.driver.find_element(*Credential.password)

    # click to sign in button
    def click_signin_meth(self):
        return self.driver.find_element(*Credential.click_sign_in).click()

    # fetch the message
    def get_message(self):
        return self.driver.find_element(*Credential.message).text
        # print(self.driver.find_element(*Credential.message).text)
