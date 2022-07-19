# Test Automation Project (TAP)

## Introduction
TAP is a simple test automation project written in python and aplying page object model. It uses Selenium as the automation framework and unittest library.
The application used as the base for the tests is GitHub website.

## Structure
TAP is structured files distributed in 3 folders:
- pages: this folder contains all the files implementing the classes that represent the pages and the elements (fields, buttons, etc).
- testdata: this folder contains just one file with a class containing only properties that represents each value used in the testes. For example, if a test searches a especific user, there is a properti in TestData class to store the value used in the search. This way if we need to change the search key, we just changed in TestData class and all the other classes will use the new value.
- tests: this folder contains the files with the tests properly saying. At this point, there is only one file called tests.py with 2 classes GitHubSearch and GitHubRepoSearch

### Pages

### TestData

### Tests

### About Page Object Model

## Running the tests
