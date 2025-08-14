
import os
from pathlib import Path
import pytest

ART_DIR = Path('artifacts')
SS_DIR = ART_DIR / 'screenshots'

def pytest_sessionstart(session):
    ART_DIR.mkdir(parents=True, exist_ok=True)
    SS_DIR.mkdir(parents=True, exist_ok=True)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Capture screenshot on test failure if a Selenium driver is present in funcargs
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            name = item.name.replace("/", "_")
            driver.save_screenshot(str(SS_DIR / f"FAIL_{name}.png"))
