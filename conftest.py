import pytest
from selenium import webdriver

driver = None

# logic to get input of city from pytest command line argument
# Use this command in terminal to run the test --> pytest test_main.py --city="city name"
def pytest_addoption(parser):
    parser.addoption("--city", action="store", default="default_city", help="City name for the test")


# Declaring setup method to deal with browser initialization
@pytest.fixture(scope="class")
def setup( request):
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # Navigate to Google
    driver.get("https://www.google.com")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

