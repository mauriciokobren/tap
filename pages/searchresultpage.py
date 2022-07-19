from element import BasePageElement
from locators import SearchResultPageLocators
from basepage import BasePage
from testdata import testdata
import logging
from selenium.webdriver.common.by import By

class SearchResultPage(BasePage):
    """GitHub Search Results page"""
    
    def __init__(self, driver):
        self.driver = driver
        logging.basicConfig(level=logging.INFO)

    """def Title_matches(self):
        "Checks if window title is the expected"
        logging.info('Title in test data is '+ testdata.TestData.GITHUB_SEARCH_WINDOW_TITLE)
        logging.info('Windows title is' + self.driver.title)
        return self.driver.title in testdata.TestData.GITHUB_SEARCH_WINDOW_TITLE
    """
    
    def Click_in_users(self):
        """Click in Users option"""
        self.users = BasePageElement(self.driver,SearchResultPageLocators.SEARCH_RESULTS_USERS_LOCATOR)
        self.users.click()

    def Result_has_user(self,user):
        """Find page title in search results page"""
        self.user = BasePageElement(self.driver,(By.LINK_TEXT,testdata.TestData.USER_FULLNAME))
        return user == self.user.text
