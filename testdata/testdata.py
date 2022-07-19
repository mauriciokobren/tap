class TestData(object):
    GITHUB_URL = "https://github.com/"
    USER_FULLNAME = 'Maurício Kobren'
    USER_NAME = "mauriciokobren"
    USER_PAGE_URL = GITHUB_URL + USER_NAME
    USER_PAGE_WINDOW_TITLE = f'{USER_NAME} ({USER_FULLNAME}) · GitHub'
    GITHUB_WINDOW_TITLE = 'GitHub'
    GITHUB_SEARCH_WINDOW_TITLE = 'Search · mauriciokobren · GitHub'
    REPO_SEARCH_KEY = 'api'
    REPO_EXPECTED_IN_SEARCH_RESULT = 'api_testing'
    REPO_SEARCH_RESULT_MESSAGE = f' 1 result for repositories matching {REPO_SEARCH_KEY} sorted by last updated '
    REPO_FILTER_BY_LANGUAGE = 'Python'
    NUMBER_OF_REPOS_FILTERED_BY_LANGUAGE = 2