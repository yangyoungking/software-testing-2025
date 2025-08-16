import yaml
import pytest
import requests
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_test.utils.driver import make_driver
from web_test.pages.login_page import LoginPage

BASE = "https://the-internet.herokuapp.com"


@pytest.fixture(scope="module")
def driver():
    """
    先探测目标站点可达性：
    - 站点 5xx 或不可达 → 跳过整模块 Selenium 测试（避免 CI 偶发失败）
    """
    try:
        r = requests.get(BASE, timeout=8)
        if r.status_code >= 500:
            pytest.skip("target site 5xx, skip selenium tests")
    except Exception as e:
        pytest.skip(f"target site unreachable: {e}")

    d = make_driver(headless=True)
    # 增加隐式等待，确保页面元素能及时加载
    d.implicitly_wait(10)  # 默认等待 10 秒
    yield d
    d.quit()


def load_creds():
    data = yaml.safe_load(
        Path('web_test/data/creds.yaml').read_text(encoding='utf-8'))
    cases = []
    for item in data.get('valid', []):
        cases.append((item['username'], item['password'], True))
    for item in data.get('invalid', []):
        cases.append((item['username'], item['password'], False))
    return cases


@pytest.mark.parametrize("username,password,expect_success", load_creds())
def test_login_variants(driver, username, password, expect_success):
    page = LoginPage(driver).open().login(username, password)
    # 使用显式等待确保 flash 消息完全加载
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))  # 替换为你实际元素的定位
    )
    msg = page.flash_text()
    if expect_success:
        assert "You logged into a secure area!" in msg
    else:
        assert "Your username is invalid!" in msg or "Your password is invalid!" in msg
