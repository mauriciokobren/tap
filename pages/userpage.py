from element import BasePageElement
from locators import RepositorySearchLocators
from basepage import BasePage
from testdata import testdata
from userrepopage import UserRepoPage
import logging

class UserPage(BasePage):
    """User page in GitHub"""

    def __init__(self, driver):
        self.driver = driver
        logging.basicConfig(level=logging.INFO)

        self.driver.get(testdata.TestData.USER_PAGE_URL)
        logging.info('Loads user page in github: '+ testdata.TestData.USER_PAGE_URL)

    #def Load(self):
    #    self.driver.get(testdata.TestData.USER_PAGE_URL) 

    def Title_matches(self):
        """Verifies that window title is correct"""
        return testdata.TestData.USER_PAGE_WINDOW_TITLE in self.driver.title

    def ClickOnRepositoriesTab(self):
        """Finds the Repositories tab in the page and click on it"""
        repo_tab = BasePageElement(self.driver,RepositorySearchLocators.REPOSITORIES_TAB)
        repo_tab.click()
        return UserRepoPage(self.driver)

