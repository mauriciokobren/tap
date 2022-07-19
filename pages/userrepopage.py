from element import BasePageElement
from locators import UserRepoPageLocators
from basepage import BasePage
from testdata import testdata
from selenium.webdriver.common.by import By
import logging

class UserRepoPage(BasePage):
    """GitHub User Repository page"""
    
    def __init__(self, driver):
        self.driver = driver
        logging.basicConfig(level=logging.INFO)
    
    def Search(self,search_text):
        self.search_field = BasePageElement(self.driver,UserRepoPageLocators.REPO_SEARCH_FIELD_LOCATOR)
        self.search_field.set_text(search_text)
        self.search_field.hit_enter()
        logging.info(f'Searches by the search key: {search_text}')

    def Repositories_in_search_results(self):
        results = self.driver.find_elements(*UserRepoPageLocators.SEARCH_RESULTS_LOCATOR)
        return len(results)
    
    def Search_result_has_text(self,text):
        """Checks that search result message is correct"""
        result_message = BasePageElement(self.driver,(By.LINK_TEXT, text))
        if result_message is not None: user_found=True 
        logging.info(f"Text '{text}' found in page: {user_found}") 
        return result_message is not None
    
    def Load(self):
        logging.info('Loading User Repository page: '+ testdata.TestData.USER_PAGE_URL+'?tab=repositories')
        self.driver.get(testdata.TestData.USER_PAGE_URL+'?tab=repositories') 
    
    def Filter_by_python_language(self):
        logging.info('Filtering repositories by Python language')
        BasePageElement(self.driver,UserRepoPageLocators.LANGUAGE_FILTER_BUTTON_LOCATOR).click()
        BasePageElement(self.driver,UserRepoPageLocators.PYTHON_LANGUAGE_LOCATOR).click()
