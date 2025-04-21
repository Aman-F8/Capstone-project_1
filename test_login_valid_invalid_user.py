import pytest
from selenium.webdriver.common.by import By
from pages.check_login_page import HomePage, LoginPage
from Config.confest import driver
from selenium.common.exceptions import WebDriverException, TimeoutException

# Valid and invalid credentials for login testing
VALID_EMAIL = "amanullahf8@gmail.com"
VALID_PASSWORD = "Aman@1995"

INVALID_EMAIL = "info@gmail.com"
INVALID_PASSWORD = "info@123"

# ---------- Test: Invalid Login ----------
def test_invalid_user_login(driver):
    """
    Test case: Attempt login with invalid credentials and check for error message.
    """
    try:
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        # Open home page
        home_page.open()

        # Attempt to log in with invalid credentials
        login_page.invalid_user_login(INVALID_EMAIL, INVALID_PASSWORD)

        # Click login button to submit form
        home_page.click_login()

        error_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'alert') or contains(@class, 'error')]")
        assert error_elements, "Expected error message for invalid login, but none found."
        print("Invalid Login Detected:", error_elements[0].text)

    except Exception as e:
        print("Test for invalid login failed due to an exception:", e)

# ---------- Test: Valid Login & Logout ----------
def test_valid_user_login_logout(driver):
    """
    Test case: Login with valid credentials, then perform logout.
    """
    try:
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        # Open home page and click login
        home_page.open()
        home_page.click_login()

        # Perform login with valid credentials
        login_page.login(VALID_EMAIL, VALID_PASSWORD)

        # Logout after successful login
        login_page.valid_logout()

    except TimeoutException as e:
        print(f"[ERROR] Timeout during valid login/logout: {e}")
        pytest.fail("Login/Logout flow failed due to timeout.")
    except Exception as e:
        print(f"[ERROR] Unexpected error in valid login/logout test: {e}")
        pytest.fail("Unexpected error in test_valid_user_login_logout.")
