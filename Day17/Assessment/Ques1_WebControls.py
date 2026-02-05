from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("Arimardan")
driver.find_element(By.NAME, "password").send_keys("SecurePass123")
driver.find_element(By.NAME, "comments").send_keys("This is a test comment.")

radio = driver.find_element(By.XPATH, "//input[@name='radioval' and @value='rd2']")
driver.execute_script("arguments[0].click();", radio)  # JS click to avoid interception

checkbox1 = driver.find_element(By.XPATH, "//input[@name='checkboxes[]' and @value='cb1']")
checkbox3 = driver.find_element(By.XPATH, "//input[@name='checkboxes[]' and @value='cb3']")
driver.execute_script("arguments[0].click();", checkbox1)
driver.execute_script("arguments[0].click();", checkbox3)

select_dropdown = Select(driver.find_element(By.NAME, "dropdown"))
select_dropdown.select_by_visible_text("Drop Down Item 3")

multi_select = Select(driver.find_element(By.NAME, "multipleselect[]"))
multi_select.select_by_visible_text("Selection Item 1")
multi_select.select_by_visible_text("Selection Item 4")


submit_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
driver.execute_script("arguments[0].click();", submit_btn)  # JS click


time.sleep(2)
print("Form submitted successfully! Check results page.")

time.sleep(3)
driver.quit()
