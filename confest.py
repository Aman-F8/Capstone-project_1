import pytest                   # Importing pytest for testing and fixture support
from selenium import webdriver  # Importing Selenium WebDriver to control the browser
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager


# Define a pytest fixture with module-level scope (runs once per module)
@pytest.fixture(scope="module")
def driver():
    '''If i try this line, i'm facing error like driver not found'''
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver = webdriver.Chrome()     # Launch a new Chrome browser instance
    driver.maximize_window()        # Maximize the browser window for better visibility

    yield driver                    # Yield the WebDriver instance to the test(s)

    driver.quit()                   # Quit the browser after all tests using this fixture are done
