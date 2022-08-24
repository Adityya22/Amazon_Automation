from selenium.webdriver.common.by import By


class Purchase:

    """
    storing the locators in a variable
    """
    buy_now = (By.XPATH, "//input[@id='buy-now-button']")

    def __init__(self, driver):
        self.driver = driver

    # click to buy now
    def buy(self):
        self.driver.find_element(*Purchase.buy_now).click()
