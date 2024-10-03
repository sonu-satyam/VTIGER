import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser",action = "store", default = "chrome")

@pytest.fixture(scope = "module")
def driver_(request):
    browser = request.config.getoption("--browser")
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported")
    driver.get("http://49.249.28.218:8888/index.php?action=Login&module=Users")

    yield driver
    driver.close()

