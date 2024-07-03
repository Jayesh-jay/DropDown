from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.imdb.com/search/name/'
        self.search_box = (By.ID, "suggestion-search")
        self.search_button = (By.ID, "suggestion-search-button")

    def open_page(self):
        self.driver.get(self.url)

    def perform_search(self, search_query):
        search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_box))
        search_box.send_keys(search_query)
        self.driver.find_element(*self.search_button).click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    imdb_search_page = IMDbSearchPage(driver)
    imdb_search_page.open_page()
    imdb_search_page.perform_search("Tom Hanks")
    # Add assertions or further actions as needed

    # Close the browser window
    driver.quit()
