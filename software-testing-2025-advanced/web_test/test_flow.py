
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from web_test.utils.driver import make_driver
from web_test.pages.dropdown_page import DropdownPage
from web_test.pages.inputs_page import InputsPage

@pytest.fixture(scope="module")
def driver():
    d = make_driver(headless=True)
    yield d
    d.quit()

def test_dropdown_and_inputs_flow(driver):
    # Dropdown
    dd = DropdownPage(driver).open().select_by_text("Option 2")
    # The site uses values '1' and '2', so we assert it's not '1'
    assert dd.selected_text() == '2'

    # Inputs page
    inputs = InputsPage(driver).open().set_value("123")
    assert inputs.get_value() == "123"
