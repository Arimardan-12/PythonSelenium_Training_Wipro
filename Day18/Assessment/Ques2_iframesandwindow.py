from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# 1. Open iframe page
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(2)

# Switch to iframe
driver.switch_to.frame("mce_0_ifr")

# Locate editable area
text_box = driver.find_element(By.ID, "tinymce")

# Clear using keyboard (correct way)
text_box.send_keys(Keys.CONTROL, "a")
text_box.send_keys(Keys.DELETE)

# Enter text
text_box.send_keys("Hello from iframe")
time.sleep(2)

# 2. Switch back to main content
driver.switch_to.default_content()

# Store parent window
parent_window = driver.current_window_handle

# 3. Open new window
driver.execute_script("window.open('https://www.google.com');")
time.sleep(2)

# 4. Switch between windows and print titles
for window in driver.window_handles:
    driver.switch_to.window(window)
    print("Window Title:", driver.title)
    time.sleep(1)

# 5. Close child window and return to parent
for window in driver.window_handles:
    if window != parent_window:
        driver.switch_to.window(window)
        driver.close()

driver.switch_to.window(parent_window)
print("Returned to Parent Window:", driver.title)

time.sleep(2)
driver.quit()
