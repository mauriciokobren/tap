# Test Automation Project (TAP)

## Introduction
TAP is a simple test automation project written in python and aplying page object model. It uses Selenium as the automation framework and unittest library.
The application used as the base for the tests is GitHub website.

## Structure
TAP is structured files distributed in 3 folders:
- _pages_: this folder contains all the files implementing the classes that represent the pages and the elements (fields, buttons, etc).
- _testdata_: this folder contains the class with all the values used in the testes
- _tests_: this folder contains the files with the tests properly saying. 

### Pages
All the classes that represent pages or page elements (fields, buttons, etc) are stored here. They contain properties representing parts of each page and also methods that are the actions the user can do in each page.
The pages available are:
- _Homepage_: represents GitHub main page
- _SearchResultPage_: represents GitHub Search Results page
- _UserPage_: model for user page in GitHub
- _UserRepoPage_: model for GitHub User Repository page

All the pages where extended from _BasePage_. At the moment no properties or methods were added to this class, but it could be the case if we need a certain behavior in all the pages. 

The _BasePageElement_ is an extension of Selenium WebElement class with additional methods _set_text(self,text)_, _get_text()_ and _hit_enter(self)_.

All the locators used to find fields, buttons or drop downs were added in classes stored in _locators.py_: _HomepageLocators, SearchResultPageLocators, RepositorySearchLocators and UserRepoPageLocators_.

The locators are defined as python tuples data type informing the type of the locator and the corresponding string. Here are some examples:
```
SEARCH_FIELD_LOCATOR = (By.NAME,'q')
REPO_SEARCH_FIELD_LOCATOR = (By.ID,'your-repos-filter')
LANGUAGE_FILTER_BUTTON_LOCATOR = (By.XPATH, '//*[@id="language-options"]/summary')
```


### TestData
All the values used in the testes are represented as methods of the class **_TestData_**. 
For example, to store the url ot GitHub the property below was created:

`GITHUB_URL = "https://github.com/"`

This property is used in many other places (mainly page classes) and also to create more complex urls.
The advantage of this technique is that if we need to change the url, we just need to chang in TestData class and all the other classes will use the new value.


### Tests
At this point, there is only one file called _tests.py_ with 2 classes:
- **_GitHubSearch_**: this class tests the Search by User in GitHub
- **_GitHubRepoSearch_**: this class tests the Repository Search starting from an user page

### About Page Object Model

### Logging
Python logging library was used to log information about the progress of each test.
To do that, first we need to import the library:
`import logging`

Then define the log level. In this case Information was used:
`logging.basicConfig(level=logging.INFO)`

Then logging.info was called each time it was interesting to inform some progress of the tests. For example:
```
def test_search_in_github(self):
  logging.info('-----------------------------------------------')
  logging.info('Starting to test search feature on GitHub')
  logging.info('Loading github homepage')
  home_page = homepage.Homepage(self.driver)
```

It's also interesting to note that the message added in each logging instruction also works as comments of the code.

## Running the tests
To run all the tests, from tap folder:

`cd tests
python test.py
`

To run just a specific test, assuming you already are in tests folder:

`python test.py Class.Desired_test`

For example: 
`python test.py GitHubRepoSearch.test_search_by_existing_repo_in_user_page`

## Next steps
The webdriver obejct is created in the _setup()_ of test classes in tests/test.py. For now Firefox browser was chosed, but more browsers could be supported, like Chrome for example.

No screenshot or video is recorded when a test fails. This can be a good resource for analysis.




