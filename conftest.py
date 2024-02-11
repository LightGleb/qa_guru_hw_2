import pytest
from selene import browser


@pytest.fixture(scope="function")
def browser_config():
    browser.config.window_height = 800
    browser.config.window_width = 1100


@pytest.fixture(scope="function")
def open_browser(browser_config):
    browser.open('https://google.com')
    yield
    browser.quit()
