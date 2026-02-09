from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

# Launch browser
driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")


# IMPLICIT WAIT
driver.implicitly_wait(10)  # waits up to 10 seconds for elements
print("Implicit wait applied")
driver.find_element(By.XPATH, "//button[text()='Enable']").click()


# EXPLICIT WAIT (element to be clickable)
wait = WebDriverWait(driver, 15)
text_box = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
)
print("Explicit wait: Element is clickable")
text_box.send_keys("Selenium Waits")


# FLUENT WAIT (with polling interval)
fluent_wait = WebDriverWait(
    driver,
    timeout=20,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)

message = fluent_wait.until(
    EC.visibility_of_element_located((By.ID, "message"))
)

# PRINT MESSAGE WHEN ELEMENT IS AVAILABLE
print("Fluent wait: Element is available for interaction")
print("Message displayed on page:", message.text)

time.sleep(3)
driver.quit()
