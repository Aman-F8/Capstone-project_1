from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Page Object for GUVI Home Page
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # Locator for the "Login" button on the homepage
        self.login_btn_locator = (By.XPATH, "//a[@class='⭐️rawbli-0 text-decoration-none me-3 text-success text-base font-medium']")

    def open(self):
        """
        Open the GUVI home page.
        """
        try:
            self.driver.get("https://www.guvi.in/")
        except Exception as e:
            print(f"Error opening GUVI home page: {e}")

    def click_login(self):
        """
        Click the login button on the home page.
        """
        try:
            login_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.login_btn_locator)
            )
            login_btn.click()
        except TimeoutException:
            print("Login button was not clickable within the timeout period.")
        except Exception as e:
            print(f"Exception while clicking login: {e}")


# Page Object for GUVI Login Page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators for login elements
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-btn")
        self.dropdown = (By.ID, "dropdown_contents")
        self.logout = (By.XPATH, "//div[contains(text(), 'Sign Out')]")
        self.error_message = (By.XPATH, "//div[@id='login_password-error' or contains(@class, 'error')]")

    def invalid_user_login(self, email, password):
        """
        Attempt login with invalid credentials.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.email_input)
            ).send_keys(email)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.password_input)
            ).send_keys(password)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.login_button)
            ).click()
        except TimeoutException:
            print("Login elements not available within timeout.")
        except Exception as e:
            print(f"Error during invalid login: {e}")

    def get_error_message(self):
        """
        Retrieve error message displayed after failed login.
        """
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.error_message)
            ).text
        except TimeoutException:
            print("Error message not visible in time.")
            return None
        except Exception as e:
            print(f"Exception while retrieving error message: {e}")
            return None

    def login(self, email, password):
        """
        Login using valid credentials.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.email_input)
            ).send_keys(email)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.password_input)
            ).send_keys(password)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.login_button)
            ).click()
        except TimeoutException:
            print("Login fields/button not available in time.")
        except Exception as e:
            print(f"Exception during valid login: {e}")

    def valid_logout(self):
        """
        Perform logout after successful login.
        """
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.dropdown)
            ).click()

            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.logout)
            ).click()
        except TimeoutException:
            print("Logout elements not clickable within the timeout.")
        except Exception as e:
            print(f"Exception during logout: {e}")
