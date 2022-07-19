from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

class BasePageElement(WebElement):
    """Base class to represent web elements"""

    def __init__(self, driver,locator):
        driver.implicitly_wait(5)
        WebDriverWait(driver, 5000).until(
            lambda driver: driver.find_element(*locator))
        element = driver.find_element(*locator)
        super().__init__(element.parent, element.id)

    def set_text(self, value):
        """Sets the text to the value supplied"""
        self.clear()
        self.send_keys(value)

    def get_text(self):
        return self.text
        
    def hit_enter(self):
        self.send_keys(Keys.RETURN)
