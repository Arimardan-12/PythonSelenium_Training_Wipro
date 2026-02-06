# locators.py
from selenium.webdriver.common.by import By

class Locators:
    # Home page
    DESKTOPS_TAB = (By.LINK_TEXT, "Desktops")
    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    # Desktops page
    MAC_ITEM = (By.LINK_TEXT, "Mac")
    SORT_DROPDOWN = (By.ID, "input-sort")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@data-original-title='Add to Cart']")
    MAC_HEADING = (By.TAG_NAME, "h2")

    # Search page
    SEARCH_DESCRIPTION_CHECKBOX = (By.NAME, "description")
