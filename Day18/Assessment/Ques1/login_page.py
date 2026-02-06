from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.ID, "submit")
    result_text = (By.TAG_NAME, "h1")

    # Reusable methods
    def enter_username(self, user):
        self.driver.find_element(*self.username).send_keys(user)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def get_result(self):
        return self.driver.find_element(*self.result_text).text
