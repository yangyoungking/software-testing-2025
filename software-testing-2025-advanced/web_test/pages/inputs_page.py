
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InputsPage:
    URL = "https://the-internet.herokuapp.com/inputs"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)
        return self

    def set_value(self, value: str):
        box = self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, "input")))
        box.clear()
        box.send_keys(str(value))
        return self

    def get_value(self):
        return self.driver.find_element(By.TAG_NAME, "input").get_attribute("value")
