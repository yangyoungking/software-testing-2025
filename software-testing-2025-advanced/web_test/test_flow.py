import pytest
import requests
from web_test.utils.driver import make_driver
from web_test.pages.dropdown_page import DropdownPage
from web_test.pages.inputs_page import InputsPage

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
    yield d
    d.quit()


def test_dropdown_and_inputs_flow(driver):
    # Dropdown
    dd = DropdownPage(driver).open().select_by_text("Option 2")
    assert dd.selected_text() == "2"  # the site uses values '1' and '2'

    # Inputs page
    inputs = InputsPage(driver).open().set_value("123")
    assert inputs.get_value() == "123"
