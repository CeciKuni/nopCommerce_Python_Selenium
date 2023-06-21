import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value setup method
    return request.config.getoption("--browser")


############## Pytest HTML Report ###########################

#Report Title
def pytest_html_report_title(report):
    report.title = "NopCommerce - Python with Selenium - Report HTML"

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Project Name": "Nop Commerce",
        "Tester": "Kuni"
    }
