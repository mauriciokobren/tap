import os,sys,time,unittest,logging
sys.path.append(os.path.abspath(os.path.join('..', 'pages')))
sys.path.append(os.path.abspath(os.path.join('..', '')))

from selenium import webdriver
from pages import homepage,userpage,userrepopage
sys.path.append(os.path.abspath(os.path.join('..', 'testdata')))
from testdata import testdata


class GitHubSearch(unittest.TestCase):
    """Simple set of tests on GitHub search"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        logging.basicConfig(level=logging.INFO)
        logging.info('Inicializing webdriver')

    def test_search_in_github(self):
        logging.info('-----------------------------------------------')
        logging.info('Starting to test search feature on GitHub')

        logging.info('Loading github homepage')
        home_page = homepage.Homepage(self.driver)
        
        logging.info('Asserting that window title is GitHub: '+str(home_page.title_matches()))
        self.assertTrue(home_page.title_matches())
        
        searchresultpage = home_page.search(testdata.TestData.USER_NAME)

        logging.info('Clicks in Users option in search result categories displayed in left side')
        searchresultpage.Click_in_users()

        user_found = searchresultpage.Result_has_user(testdata.TestData.USER_FULLNAME)
        self.assertTrue(user_found)
        logging.info(f'Asserting that expected user was found in search results: {user_found}')
        logging.info('Tests the search feature on GitHub is completed')
        logging.info('-----------------------------------------------')

    def tearDown(self):
        self.driver.quit()

class GitHubRepoSearch(unittest.TestCase):
    """Simple test on GitHub Repository Search"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        logging.basicConfig(level=logging.INFO)
        logging.info('Inicializing webdriver')

    def test_search_by_existing_repo_in_user_page(self):
        logging.info('----------------------------------------------------------')
        logging.info('Starting to test the repository search on GitHub user page')
        user_page = userpage.UserPage(self.driver)
        
        logging.info('Window title is GitHub:' + str(user_page.Title_matches()))
        self.assertTrue(user_page.Title_matches())

        logging.info('Click on Repositories Tab')
        userrepositorypage = user_page.ClickOnRepositoriesTab()
        userrepositorypage.Search(testdata.TestData.REPO_SEARCH_KEY)
        
        repo_found = userrepositorypage.Search_result_has_text(testdata.TestData.REPO_EXPECTED_IN_SEARCH_RESULT)
        self.assertTrue(repo_found)
        logging.info(f'Repository found in search results: {repo_found}')
        
        logging.info('Test of repository search on GitHub user page is completed')
        logging.info('----------------------------------------------------------')

    def test_filter_repo_by_language(self):
        logging.info('----------------------------------------------------------')
        logging.info('Starting to test filtering repositories of user page by language')

        logging.info('Create UserRepoPage object and load repository page')
        userrepositorypage = userrepopage.UserRepoPage(self.driver)
        userrepositorypage.Load()
        userrepositorypage.Filter_by_python_language()

        number_of_repos = userrepositorypage.Repositories_in_search_results()
        logging.info(f'Number of repositories in search results page: {number_of_repos}')
        self.assertTrue( number_of_repos == testdata.TestData.NUMBER_OF_REPOS_FILTERED_BY_LANGUAGE)
        logging.info('Asserting the number of repositories is the expected:'+
            str(number_of_repos == testdata.TestData.NUMBER_OF_REPOS_FILTERED_BY_LANGUAGE))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()