

from element import BasePageElement
from locators import MainPageLocators
from page import BasePage


class UserPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""
# action: ClickOnRepositoriesTab()
# action: Search(searchkey: string)
# action: FilterbyLanguage(language: string)
# action: FilterbyType(type: string)

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

