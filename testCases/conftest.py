import pytest
from selenium.webdriver import Chrome, ChromeOptions, Firefox, Ie, Edge, DesiredCapabilities, Remote


@pytest.fixture(scope="module")
def browser():
    # chrome_options = ChromeOptions()
    # prefs = {
    #     'download.default_directory': 'C:\\my\\auto\\web\\web_pytest_refactor\\'
    # }
    # chrome_options.add_experimental_option('prefs', prefs)
    # # chrome_options.add_argument("--headless")
    #
    # # close window "chrome is being controlled by..."
    # # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # driver = Chrome(options=chrome_options)

    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
