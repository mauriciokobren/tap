from selenium.webdriver.common.by import By

class HomepageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SEARCH_FIELD_LOCATOR = (By.NAME,'q')

class SearchResultPageLocators(object):
    """Locators for Search Results page"""
    SEARCH_RESULTS_USERS_LOCATOR = (By.XPATH, '/html/body/div[4]/main/div/div[2]/nav[1]/a[10]')
    SEARCH_RESULTS_PAGE_TITLE_LOCATOR = (By.XPATH,'//*[@id="js-pjax-container"]/div/div[3]/div/div[1]')

class RepositorySearchLocators(object):
    """Locators for Repository Locators Search  """
    REPOSITORIES_TAB = (By.XPATH,'/html/body/div[4]/main/div[1]/div/div/div[2]/div/nav/a[2]')

class UserRepoPageLocators(object):
    """Locators for repository search results page"""
    REPO_SEARCH_FIELD_LOCATOR = (By.ID,'your-repos-filter')
    SEARCH_RESULTS_LOCATOR = (By.XPATH,'/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[2]/div/ul/li')
    SEARCH_RESULTS_MESSAGE_LOCATOR = (By.XPATH,'//*[@id="user-repositories-list"]/div[1]/div[1]')
    LANGUAGE_FILTER_BUTTON_LOCATOR = (By.XPATH, '//*[@id="language-options"]/summary')
    PYTHON_LANGUAGE_LOCATOR =(By.XPATH,'//*[@id="language-options"]/details-menu/div/div/label[2]/span')
    