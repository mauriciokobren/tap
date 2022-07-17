from element import BasePageElement
from locators import HomepageLocators
from basepage import BasePage
from testdata import testdata
from searchresultpage import SearchResultPage

class Homepage(BasePage):
    """GitHub main page"""

    def __init__(self, driver):
        self.driver = driver
        """Creating the element for the search field"""
        self.search_field = BasePageElement(driver,HomepageLocators.SEARCH_FIELD_LOCATOR)

    def title_matches(self):
        """Verifies that window title is correct"""
        return testdata.TestData.GITHUB_WINDOW_TITLE in self.driver.title

    def search(self,search_text):
        self.search_field.set_text(search_text)
        self.search_field.hit_enter()
        return SearchResultPage(self.driver)
