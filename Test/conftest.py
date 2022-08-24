import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from config.configuration import TestConfig


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--email", action="store", help="abcd@test.com")
    parser.addoption("--password", action="store", help="12345678")
    parser.addoption("--search_item", action="store", help="mobile")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    # creating Chrome browser object
    chrome_options = webdriver.ChromeOptions()

    # creating firefox browser object
    firefox_options = webdriver.FirefoxOptions()

    # creating edge browser object
    edge_options = webdriver.EdgeOptions()

    chrome_options.add_argument('--ignore-certificate-error')

    # select the browser to use
    if browser_name == "chrome":
        s = Service(TestConfig.chrome_executable_path)
        driver = webdriver.Chrome(service=s, options=chrome_options)
    elif browser_name == "firefox":
        s = Service(TestConfig.firefox_executable_path)
        driver = webdriver.Firefox(service=s, options=firefox_options)
    elif browser_name == "firefox":
        s = Service(TestConfig.edge_executable_path)
        driver = webdriver.Chrome(service=s, options=edge_options)

    # get the base-url title
    driver.get(TestConfig.base_url)

    # maximize the window
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.quit()


@pytest.fixture
def params(request):
    params = {'email': request.config.getoption('--email'),
              'password': request.config.getoption('--password'),
              'search_item': request.config.getoption('--search_item')}

    if params['email'] is None and params['password'] is None:
        pytest.skip()

    return params
