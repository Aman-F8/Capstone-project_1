import requests
import pytest
from data.Data import URL, LOGIN_URL, EXPECTED_TITLE
from pages.page_access import HomePage, LoginPage
from Config.confest import driver

def test_tc1_check_url(driver):
    """
    Test Case 1: Check if the base GUVI URL is reachable (status code 200)
    """
    try:
        response = requests.get(URL)
        assert response.status_code == 200, f"[FAIL] URL not reachable: {URL}"
    except requests.RequestException as e:
        print(f"[ERROR] Request to {URL} failed: {e}")
        pytest.fail("Network issue or invalid URL")


def test_tc2_page_title(driver):
    """
    Test Case 2: Validate the page title matches the expected title
    """
    try:
        driver.get(URL)
        assert driver.title == EXPECTED_TITLE, f"[FAIL] Title mismatch: Expected '{EXPECTED_TITLE}', Got '{driver.title}'"
    except Exception as e:
        print(f"[ERROR] Page title test failed: {e}")
        pytest.fail("Could not load page or incorrect title")


def test_tc3_login_button(driver):
    """
    Test Case 3: Check if the login button is visible and clickable
    """
    try:
        login_page = LoginPage(driver)
        login_page.open(LOGIN_URL)
        assert login_page.check_login_button(), "[FAIL] Login button not visible or clickable"
    except Exception as e:
        print(f"[ERROR] Login button check failed: {e}")
        pytest.fail("Could not verify login button")


def test_tc4_signup_button(driver):
    """
    Test Case 4: Check if the signup button is visible and clickable on the home page
    """
    try:
        home_page = HomePage(driver)
        home_page.open(URL)
        assert home_page.check_signup_button(), "[FAIL] Signup button not visible or clickable"
    except Exception as e:
        print(f"[ERROR] Signup button check failed: {e}")
        pytest.fail("Could not verify signup button")


def test_tc5_login_page_exists():
    """
    Test Case 5: Ensure that the login page URL returns a valid HTTP response
    """
    try:
        response = requests.get(LOGIN_URL)
        assert response.status_code == 200, f"[FAIL] Login URL not reachable: {LOGIN_URL}"
    except requests.RequestException as e:
        print(f"[ERROR] Request to {LOGIN_URL} failed: {e}")
        pytest.fail("Login page not available or network error")
