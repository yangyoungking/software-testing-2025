
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)
        return self

    def select_by_text(self, text: str):
        dropdown_el = self.wait.until(EC.element_to_be_clickable((By.ID, "dropdown")))
        Select(dropdown_el).select_by_visible_text(text)
        return self

    def selected_text(self):
        dropdown_el = self.driver.find_element(By.ID, "dropdown")
        return dropdown_el.get_attribute("value")  # '1' or '2'
