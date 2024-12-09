import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
    # Tự động quản lý ChromeDriver
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

#test register successfully
def test_register_successfully(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='login-form']/a").click()
    driver.find_element(By.XPATH,"//*[@id='name']").send_keys("tester")
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys("tester111@gmail.com")
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("123456789")
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/form/div/div/button").click()
    link="http://localhost/ProjectWeb/login.html"
    assert link==driver.current_url,"Failed to register"

#test account is registered
def test_account_is_registered(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='login-form']/a").click()
    driver.find_element(By.XPATH,"//*[@id='name']").send_keys("tester")
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys("tester111@gmail.com")
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("123456789")
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/form/div/div/button").click()
    link="http://localhost/ProjectWeb/xulySigup.php"
    time.sleep(2)
    assert link==driver.current_url

#test blank in fullname
def test_account_blank_fullname(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='login-form']/a").click()
    driver.find_element(By.XPATH,"//*[@id='name']").send_keys("")
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys("tester111@gmail.com")
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("123456789")
    driver.find_element(By.XPATH,"/html/body/form/div/div/button").click()
    wait = WebDriverWait(driver, 10)
    message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-msg"))).text
    time.sleep(2)
    assert message == "Tên Không Hợp Lệ"

#test blank in gmail
def test_account_blank_gmail(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='login-form']/a").click()
    driver.find_element(By.XPATH,"//*[@id='name']").send_keys("tester")
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys("")
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("123456789")
    driver.find_element(By.XPATH,"/html/body/form/div/div/button").click()
    wait = WebDriverWait(driver, 10)
    message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-msg"))).text
    time.sleep(2)
    assert message == "Vui Lòng Nhập Email"

#test blank in username
def test_account_blank_username(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='login-form']/a").click()
    driver.find_element(By.XPATH,"//*[@id='name']").send_keys("tester")
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys("tester111@gmail.com")
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("123456789")
    driver.find_element(By.XPATH,"/html/body/form/div/div/button").click()
    wait = WebDriverWait(driver, 10)
    message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-msg"))).text
    time.sleep(2)
    assert message == "Tên Đăng Nhập Không Hợp Lệ" 

#test blank in password
def test_account_blank_password(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='login-form']/a").click()
    driver.find_element(By.XPATH,"//*[@id='name']").send_keys("tester")
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys("tester111@gmail.com")
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("")
    driver.find_element(By.XPATH,"/html/body/form/div/div/button").click()
    wait = WebDriverWait(driver, 10)
    message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-msg"))).text
    time.sleep(2)
    assert message == "Mật Khẩu Phải Có Ít Nhất 8 Kí Tự" 

#test email without .com
def test_email_without_com(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='login-form']/a").click()
    driver.find_element(By.XPATH,"//*[@id='name']").send_keys("tester")
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys("tester111@gmail")
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("123456789")
    driver.find_element(By.XPATH,"/html/body/form/div/div/button").click()
    wait = WebDriverWait(driver, 10)
    message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-msg"))).text
    time.sleep(2)
    assert message == "Email Không Hợp Lệ"

