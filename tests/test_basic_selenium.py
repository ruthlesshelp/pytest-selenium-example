from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException


def test_title(chrome_browser):
    """
    Test the title of the Python.org website
    """
    chrome_browser.get("https://www.python.org")
    assert chrome_browser.title == "Welcome to Python.org"


def test_search(chrome_browser):
    """
    Test the search functionality of the DuckDuckGo website
    """
    url = "https://duckduckgo.com/"
    search_term = "RuthlessHelp github"
    # Navigate to the Google home page.
    chrome_browser.get(url)

    # Find the search box using its name attribute value.
    search_box = chrome_browser.find_element(By.ID, value="searchbox_input")

    # Enter a search query and submit.
    search_box.send_keys(search_term + Keys.RETURN)

    # Assert that the title contains the search term.
    assert search_term in chrome_browser.title
