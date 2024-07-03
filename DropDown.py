from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IMDbSearchPage:
    def __init__(self, driver):
        # Initialize the driver and set the URL and locators
        self.driver = driver
        self.url = 'https://www.imdb.com/search/name/'
        self.search_box = (By.ID, "suggestion-search")
        self.search_button = (By.ID, "suggestion-search-button")

    def open_page(self):
        # Open the IMDb search page
        self.driver.get(self.url)

    def perform_search(self, search_query):
        # Wait for the search box to be present and enter the search query
        search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_box))
        search_box.send_keys(search_query)
        # Click the search button
        self.driver.find_element(*self.search_button).click()


if __name__ == "__main__":
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    # Create an instance of IMDbSearchPage
    imdb_search_page = IMDbSearchPage(driver)

    # Open the IMDb search page
    imdb_search_page.open_page()

    # Perform a search for "Tom Hanks"
    imdb_search_page.perform_search("Tom Hanks")

    # Add assertions or further actions as needed
    # For example, you can wait for search results to load and verify them
    try:
        # Example: Wait for a search result to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "lister-item")))
        print("Search results loaded successfully")
    except:
        print("Failed to load search results")

    # Close the browser window
    driver.quit()
