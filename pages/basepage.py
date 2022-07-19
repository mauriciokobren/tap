from element import BasePageElement

class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

