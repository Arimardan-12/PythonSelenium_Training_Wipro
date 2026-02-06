# test_opencart.py
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from .locators import Locators

class TestOpencart:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demo.opencart.com/")

    def teardown_method(self):
        self.driver.quit()

    def test_desktop_and_search_flow(self):
        driver = self.driver

        # 1. Click on Desktops tab
        driver.find_element(*Locators.DESKTOPS_TAB).click()

        # 2. Click on Mac
        driver.find_element(*Locators.MAC_ITEM).click()

        # 3. Verify Mac heading
        mac_heading = driver.find_element(*Locators.MAC_HEADING).text
        assert mac_heading == "Mac"

        # 4. Sort by Name (A-Z)
        sort_element = driver.find_element(*Locators.SORT_DROPDOWN)
        Select(sort_element).select_by_visible_text("Name (A - Z)")

        # 5. Add to Cart
        driver.find_element(*Locators.ADD_TO_CART_BUTTON).click()

        # 6. Search for "Monitors"
        search_box = driver.find_element(*Locators.SEARCH_BOX)
        search_box.clear()  # Clear previous text
        search_box.send_keys("Monitors")
        driver.find_element(*Locators.SEARCH_BUTTON).click()

        # 7. Clear search box again for next search
        search_box = driver.find_element(*Locators.SEARCH_BOX)
        search_box.clear()

        # 8. Search with description checkbox
        search_box.send_keys("Monitors")
        driver.find_element(*Locators.SEARCH_DESCRIPTION_CHECKBOX).click()
        driver.find_element(*Locators.SEARCH_BUTTON).click()
