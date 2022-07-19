from element import BasePageElement
from locators import HomepageLocators
from basepage import BasePage
from testdata import testdata
from searchresultpage import SearchResultPage
import logging

class Homepage(BasePage):
    """GitHub main page"""

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(testdata.TestData.GITHUB_URL)
        logging.basicConfig(level=logging.INFO)
        logging.info('github homepage loaded: '+ testdata.TestData.GITHUB_URL)
        
        self.search_field = BasePageElement(driver,HomepageLocators.SEARCH_FIELD_LOCATOR)
        logging.info('Element for the search field created')

    def load(self):
        self.driver.get(testdata.TestData.GITHUB_URL) 

    def title_matches(self):
        """Verifies that window title is correct"""
        return testdata.TestData.GITHUB_WINDOW_TITLE in self.driver.title

    def search(self,search_text):
        self.search_field.set_text(search_text)
        logging.info(f'Search text entered in search field: {search_text}')
        
        self.search_field.hit_enter()
        return SearchResultPage(self.driver)
