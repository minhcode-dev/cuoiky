import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import login as l
@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

#login successfully
def test_login(driver):
    l.login(driver)
    time.sleep(5)
    assert driver.current_url=="http://localhost/ProjectWeb/index.php","Failed to login"

#login wrong password
def test_login_wrong_password(driver):
    l.login_wrong_pass(driver)
    try:
        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='error-msg']"))
        ).text
        assert error_msg == "Sai tên đăng nhập hoặc mật khẩu", f"Expected 'Sai tên đăng nhập hoặc mật khẩu', but got '{error_msg}'"
    except Exception as e:
        assert False, f"Error message not found or didn't appear in time: {str(e)}"

def test_login_blank_pass(driver):
    l.login_wrong_pass(driver)
    try:
        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='error-msg']"))
        ).text
        assert error_msg == "Sai tên đăng nhập hoặc mật khẩu", f"Expected 'Sai tên đăng nhập hoặc mật khẩu', but got '{error_msg}'"
    except Exception as e:
        assert False, f"Error message not found or didn't appear in time: {str(e)}"

#login wrong username
def test_login_wrong_username(driver):
    l.login_wrong_user(driver)
    try:
        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='error-msg']"))
        ).text
        assert error_msg == "Sai tên đăng nhập hoặc mật khẩu", f"Expected 'Sai tên đăng nhập hoặc mật khẩu', but got '{error_msg}'"
    except Exception as e:
        assert False, f"Error message not found or didn't appear in time: {str(e)}"

def test_login_blank_username(driver):
    l.login_wrong_user(driver)
    try:
        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='error-msg']"))
        ).text
        assert error_msg == "Sai tên đăng nhập hoặc mật khẩu", f"Expected 'Sai tên đăng nhập hoặc mật khẩu', but got '{error_msg}'"
    except Exception as e:
        assert False, f"Error message not found or didn't appear in time: {str(e)}"

#login blank all 
def test_login_blank_all(driver):
    l.login_blank_all(driver)
    try:
        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='error-msg']"))
        ).text
        assert error_msg == "Sai tên đăng nhập hoặc mật khẩu", f"Expected 'Sai tên đăng nhập hoặc mật khẩu', but got '{error_msg}'"
    except Exception as e:
        assert False, f"Error message not found or didn't appear in time: {str(e)}"
