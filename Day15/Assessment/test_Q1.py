from selenium import webdriver
import time

def test_open_website():
    # 1. Open Chrome browser
    driver = webdriver.Chrome()

    # 2. Navigate to a website
    driver.get("https://www.wikipedia.org")

    # 3. Print page title and URL
    print("Page Title:", driver.title)
    print("Current URL:", driver.current_url)

    time.sleep(2)

    # 4. Close the browser
    driver.quit()
