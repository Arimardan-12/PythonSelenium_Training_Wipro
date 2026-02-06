"""Consider the flow mentioned in Lab 3 & Lab 4, complete the task using page object model and page factory."""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class HomePage:
    """Page Object: Locators and Actions"""

    def __init__(self, driver):
        self.driver = driver

    # ------------------- Locators -------------------
    desktops_tab = (By.LINK_TEXT, "Desktops")
    mac_link = (By.LINK_TEXT, "Mac")
    sort_dropdown = (By.ID, "input-sort")
    add_to_cart_button = (By.XPATH, "//button[contains(@onclick,'cart.add')]")
    search_box = (By.NAME, "search")
    search_button = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
    product_description_checkbox = (By.NAME, "description")
    page_heading = (By.TAG_NAME, "h2")

    # ------------------- Actions -------------------
    def go_to_desktops(self):
        self.driver.find_element(*self.desktops_tab).click()

    def select_mac(self):
        self.driver.find_element(*self.mac_link).click()

    def verify_mac_heading(self):
        heading = self.driver.find_element(*self.page_heading).text
        assert heading == "Mac", f"Expected 'Mac' heading but got {heading}"

    def sort_by_name_az(self):
        Select(self.driver.find_element(*self.sort_dropdown)).select_by_visible_text("Name (A - Z)")

    def add_mac_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def search_product(self, product_name, description=False):
        box = self.driver.find_element(*self.search_box)
        box.clear()
        box.send_keys(product_name)
        if description:
            self.driver.find_element(*self.product_description_checkbox).click()
        self.driver.find_element(*self.search_button).click()


class TestLab3And4:
    """Test Cases for Lab 3 & Lab 4"""

    def setup_method(self):
        self.driver = webdriver.Firefox()  # Or Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://demo.opencart.com/")
        self.home = HomePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    # ----- Lab 3 Flow -----
    def test_lab3_flow(self):
        self.home.go_to_desktops()
        self.home.select_mac()
        self.home.sort_by_name_az()
        self.home.add_mac_to_cart()

    # ----- Lab 4 Flow -----
    def test_lab4_flow(self):
        self.home.go_to_desktops()
        self.home.select_mac()
        self.home.verify_mac_heading()
        self.home.sort_by_name_az()
        self.home.add_mac_to_cart()

        # Search for Monitors
        self.home.search_product("Monitors")
        self.home.search_product("Monitors", description=True)


# Run tests directly if needed
if __name__ == "__main__":
    pytest.main(["-v", "Lab3And4_SingleFile.py"])
