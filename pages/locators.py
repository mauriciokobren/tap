from selenium.webdriver.common.by import By

class HomepageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SEARCH_FIELD_LOCATOR = (By.NAME,'q')

class SearchResultPageLocators(object):
    "Locators for Search Results page"
    SEARCH_RESULTS_USERS_LOCATOR = (By.XPATH, '/html/body/div[4]/main/div/div[2]/nav[1]/a[10]')
    #SEARCH_RESULTS_PAGE_TITLE_LOCATOR = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[1]/h3')
    SEARCH_RESULTS_PAGE_TITLE_LOCATOR = (By.XPATH,'//*[@id="js-pjax-container"]/div/div[3]/div/div[1]')

class SearchRepositoriesLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass