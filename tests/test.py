import os,sys,time
sys.path.append(os.path.abspath(os.path.join('..', 'pages')))
sys.path.append(os.path.abspath(os.path.join('..', '')))
import unittest
from selenium import webdriver
from pages import homepage

sys.path.append(os.path.abspath(os.path.join('..', 'testdata')))
from testdata import testdata


class GitHubSearch(unittest.TestCase):
    """Simple set of tests on GitHub search"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(testdata.TestData.GITHUB_URL)

    def test_search_in_github(self):
        """Tests the search feature on GitHub"""

        """Loads github homepage"""
        mainpage = homepage.Homepage(self.driver)
        
        """Asserts that window title is GitHub"""
        self.assertTrue(mainpage.title_matches(), "page title doesn't match.")
        """Searches by value stored in USER_NAME and returns search result page"""
        searchresultpage = mainpage.search(testdata.TestData.USER_NAME)
        """Assets that window title is correct in search results page"""
        self.assertTrue(searchresultpage.title_matches(), "page title doesn't match.")
        """Clicks in Users option in search result categories displayed in left side"""
        searchresultpage.click_in_users()
        """Asserts that the User Name used in the search is displayed in search results"""
        self.assertTrue(searchresultpage.result_has_user(testdata.TestData.USER_FULLNAME))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()