from selenium import webdriver
from login_page import LoginPage
import config

def test_login():
    driver = webdriver.Chrome()
    driver.get(config.URL)
    driver.maximize_window()

    page = LoginPage(driver)

    page.enter_username(config.USERNAME)
    page.enter_password(config.PASSWORD)
    page.click_login()

    result = page.get_result()

    assert result == config.EXPECTED_RESULT
    print("Test Passed: Result Verified")

    driver.quit()
