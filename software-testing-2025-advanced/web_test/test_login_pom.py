
import yaml
import pytest
from pathlib import Path
from selenium.webdriver.common.by import By
from web_test.utils.driver import make_driver
from web_test.pages.login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    d = make_driver(headless=True)
    yield d
    d.quit()

def load_creds():
    data = yaml.safe_load(Path('web_test/data/creds.yaml').read_text(encoding='utf-8'))
    cases = []
    for item in data.get('valid', []):
        cases.append((item['username'], item['password'], True))
    for item in data.get('invalid', []):
        cases.append((item['username'], item['password'], False))
    return cases

@pytest.mark.parametrize("username,password,expect_success", load_creds())
def test_login_variants(driver, username, password, expect_success):
    page = LoginPage(driver).open().login(username, password)
    msg = page.flash_text()
    if expect_success:
        assert "You logged into a secure area!" in msg
    else:
        assert "Your username is invalid!" in msg or "Your password is invalid!" in msg
