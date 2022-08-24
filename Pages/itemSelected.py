from selenium.webdriver.common.by import By


class Item_Selected:
    """
    storing the locators in a variable
    """
    result = (By.TAG_NAME, "h2")
    second = (By.XPATH, "(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style "
                        "a-text-normal'])[2]")

    def __init__(self, driver):
        self.driver = driver

    # get all the name of product shown after search
    def get_result(self):
        all_result = self.driver.find_elements(*Item_Selected.result)
        return all_result

    # click to the fourth product
    def click_second(self):
        return self.driver.find_element(*Item_Selected.second).click()

    # switch to the newly opened windows
    def frame_switch(self):
        windows_opened = self.driver.window_handles
        print(len(windows_opened))
        return self.driver.switch_to.window(windows_opened[1])

    # scroll down to buy now option button
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,700);")
