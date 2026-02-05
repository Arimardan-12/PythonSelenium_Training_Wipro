from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://letcode.in/alert")
driver.find_element(By.ID,"accept").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()

driver.find_element(By.ID,"confirm").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()

driver.find_element(By.ID, "prompt").click()
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Arimardan Singh")
alert.accept()
result_text = driver.find_element(By.ID, "myName").text
print("Text entered in prompt alert:", result_text)


driver.quit()

