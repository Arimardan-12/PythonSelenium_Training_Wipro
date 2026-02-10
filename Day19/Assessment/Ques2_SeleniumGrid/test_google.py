#testgoogle.py
import pytest
from Day19.Assessment.Ques2_SeleniumGrid.driverfactory import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_google_parallel(browser):
    driver = get_driver(browser)

    # Print browser and platform details
    browser_name = driver.capabilities.get("browserName")
    platform = driver.capabilities.get("platformName")
    print(f"Running on Browser: {browser_name}, Platform: {platform}")

    # Navigate to website
    driver.get("https://www.google.com")

    # Wait for search box
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.NAME, "q")))

    # Verify page title
    assert "Google" in driver.title

    driver.quit()
