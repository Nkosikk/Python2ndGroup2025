import time

import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()

    elif browser.lower() == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Safari()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
