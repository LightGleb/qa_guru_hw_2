import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_config():
    browser.config.window_height = 800
    browser.config.window_width = 600
    browser.config.base_url = "https://google.com"
    yield
    browser.quit()
