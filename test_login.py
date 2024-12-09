import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

#login successfully
def test_login(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("123456789")
    driver.find_element(By.CLASS_NAME,"submit-btn").click()
    time.sleep(5)
    assert driver.current_url=="http://localhost/ProjectWeb/index.php","Failed to login"

#login wrong password or blank
def test_login_wrong_password(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("123")
    driver.find_element(By.CLASS_NAME,"submit-btn").click()
    try:
        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='error-msg']"))
        ).text
        assert error_msg == "Sai tên đăng nhập hoặc mật khẩu", f"Expected 'Sai tên đăng nhập hoặc mật khẩu', but got '{error_msg}'"
    except Exception as e:
        assert False, f"Error message not found or didn't appear in time: {str(e)}"

#login wrong username or blank
def test_login_wrong_username(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tester11")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("123456789")
    driver.find_element(By.CLASS_NAME,"submit-btn").click()
    try:
        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='error-msg']"))
        ).text
        assert error_msg == "Sai tên đăng nhập hoặc mật khẩu", f"Expected 'Sai tên đăng nhập hoặc mật khẩu', but got '{error_msg}'"
    except Exception as e:
        assert False, f"Error message not found or didn't appear in time: {str(e)}"

#login blank all 
def test_login_blank_all(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("")
    driver.find_element(By.CLASS_NAME,"submit-btn").click()
    try:
        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='error-msg']"))
        ).text
        assert error_msg == "Sai tên đăng nhập hoặc mật khẩu", f"Expected 'Sai tên đăng nhập hoặc mật khẩu', but got '{error_msg}'"
    except Exception as e:
        assert False, f"Error message not found or didn't appear in time: {str(e)}"
