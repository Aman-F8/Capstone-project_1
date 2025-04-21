from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

# BasePage: Contains common functions shared across all pages
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Create a default wait object with a timeout of 10 seconds
        self.wait = WebDriverWait(driver, 10)
        # Locator for login button (used optionally in base)
        self.login_button = (By.ID, "login-btn")

    def open(self, url):
        """
        Open a given URL in the browser.
        """
        try:
            self.driver.get(url)
        except WebDriverException as e:
            print(f"[ERROR] Could not open URL: {url}. Exception: {e}")

    def is_element_visible(self, by_locator):
        """
        Check if an element is visible on the page.
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except TimeoutException:
            print(f"[ERROR] Element {by_locator} not visible within timeout.")
            return False
        except Exception as e:
            print(f"[ERROR] Exception checking visibility of {by_locator}: {e}")
            return False

    def is_element_clickable(self, by_locator):
        """
        Check if an element is clickable.
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
            return True if element else False
        except TimeoutException:
            print(f"[ERROR] Element {by_locator} not clickable within timeout.")
            return False
        except Exception as e:
            print(f"[ERROR] Exception checking clickability of {by_locator}: {e}")
            return False

    def click_login(self):
        """
        Click on the login button (common method).
        """
        try:
            login_btn = self.wait.until(EC.element_to_be_clickable(self.login_button))
            login_btn.click()
        except TimeoutException:
            print(f"[ERROR] Login button not clickable within timeout.")
        except Exception as e:
            print(f"[ERROR] Exception while clicking login button: {e}")


# HomePage: Specific methods for GUVI home page
class HomePage(BasePage):
    # Locator for the "Sign Up" button
    SIGNUP_BUTTON = (By.XPATH,
        "//a[@class='⭐️rawbli-0 bg-green-500 hover:bg-green-600 text-white font-normal py-2 px-4 rounded text-base min-h-8 h-8 align-middle mr-2']"
    )

    def check_signup_button(self):
        """
        Validate if the Sign Up button is both visible and clickable.
        """
        try:
            return self.is_element_visible(self.SIGNUP_BUTTON) and self.is_element_clickable(self.SIGNUP_BUTTON)
        except Exception as e:
            print(f"[ERROR] Error checking Sign Up button: {e}")
            return False


# LoginPage: Specific methods for login functionality
class LoginPage(BasePage):
    # Locator for login button
    LOGIN_BUTTON = (By.ID, "login-btn")

    def check_login_button(self):
        """
        Validate if the Login button is both visible and clickable.
        """
        try:
            return self.is_element_visible(self.LOGIN_BUTTON) and self.is_element_clickable(self.LOGIN_BUTTON)
        except Exception as e:
            print(f"[ERROR] Error checking Login button: {e}")
            return False









