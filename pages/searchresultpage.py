from element import BasePageElement
from locators import SearchResultPageLocators
from basepage import BasePage
from testdata import testdata
import time

class SearchResultPage(BasePage):
    """GitHub Search Results page"""
    
    def __init__(self, driver):
        self.driver = driver
        self.users = BasePageElement(driver,SearchResultPageLocators.SEARCH_RESULTS_USERS_LOCATOR)

    def title_matches(self):
        """Checks if window title is the expected"""
        return testdata.TestData.GITHUB_SEARCH_WINDOW_TITLE in self.driver.title
    
    def click_in_users(self):
        """Click in Users option"""
        self.users.click()

    def result_has_user(self,user):
        """Find page title in search results page"""
        return user in self.driver.page_source

    def go_to_users(self,user):
        """Triggers the search"""
        self.users.click()
        element = self.driver.find_element(By.LINK_TEXT, user)
        element.click()
