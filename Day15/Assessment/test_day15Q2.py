import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDay15Q2:

    def setup_method(self, method):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def teardown_method(self, method):
        self.driver.quit()

    def test_day15Q1(self):
        # Step 1: Open URL
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


        username = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "username"))
        )
        username.send_keys("Admin")


        password = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        password.send_keys("admin123")


        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_btn.click()


        dashboard = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )

        assert dashboard.text == "Dashboard"
