from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

class BasePageElement(WebElement):
    """Base class to represent web elements"""

    def __init__(self, driver,locator):
        WebDriverWait(driver, 5000).until(
            lambda driver: driver.find_element(*locator))
        self.element = driver.find_element(*locator)

    def set_text(self, value):
        """Sets the text to the value supplied"""
        self.element.clear()
        self.element.send_keys(value)

    def get_text(self):
        self.element.text
        
    def click(self):
        self.element.click()

    def hit_enter(self):
        self.element.send_keys(Keys.RETURN)
