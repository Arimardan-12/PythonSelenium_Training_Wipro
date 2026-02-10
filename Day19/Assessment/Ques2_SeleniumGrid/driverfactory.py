"""	Selenium Grid Execution
	Write a Selenium script that:
	1. Connects to Selenium Grid using RemoteWebDriver
	2. Runs the same test on multiple browsers
	3. Navigates to a website and verifies the page title
	4. Prints browser name and platform for each execution"""

#driverfactory.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

GRID_URL = "http://10.173.92.215:4444"

def get_driver(browser):
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    elif browser == "edge":
        options = EdgeOptions()
    else:
        raise ValueError("Browser not supported")

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )
    return driver
