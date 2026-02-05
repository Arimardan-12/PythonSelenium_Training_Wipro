from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#simple alert
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://letcode.in/alert")
time.sleep(2)
driver.find_element(By.ID, "accept").click()
time.sleep(1)
alert = driver.switch_to.alert
print("Simple Alert says:", alert.text)
alert.accept()
time.sleep(1)

#confirm alert
driver.find_element(By.ID, "confirm").click()
time.sleep(1)
confirm = driver.switch_to.alert
print("Confirm Alert says:", confirm.text)
confirm.dismiss()
time.sleep(1)

#prompt alert
driver.find_element(By.ID, "prompt").click()
time.sleep(1)
prompt = driver.switch_to.alert
print("Prompt Alert says:", prompt.text)
prompt.send_keys("Arimardan Singh")
time.sleep(1)
prompt.accept()
time.sleep(1)
result_text = driver.find_element(By.ID, "myName").text
print("Displayed result:", result_text)
driver.quit()
