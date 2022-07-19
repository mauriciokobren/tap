# Test Automation Project (TAP)

## Introduction
TAP is a simple test automation project written in python and aplying page object model. It uses Selenium as the automation framework and unittest library.
The application used as the base for the tests is GitHub website.

## Structure
TAP is structured files distributed in 3 folders:
- pages: this folder contains all the files implementing the classes that represent the pages and the elements (fields, buttons, etc).
- testdata: this folder contains the class with all the values used in the testes
- tests: this folder contains the files with the tests properly saying. 

### Pages

### TestData
All the values used in the testes are represented as methods of the class **_TestData_**. 
For example, to store the url ot GitHub the property below was created:

`GITHUB_URL = "https://github.com/"`

This property is used in many other places (mainly page classes) and also to create more complex urls.
The advantage of this technique is that if we need to change the url, we just need to chang in TestData class and all the other classes will use the new value.


### Tests
At this point, there is only one file called tests.py with 2 classes GitHubSearch and GitHubRepoSearch

### About Page Object Model

## Running the tests
