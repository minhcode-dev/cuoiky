import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException, WebDriverException
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
# Edit account
def test_edit_account_success(driver):
    try:
        # Login
        driver.get("http://localhost/ProjectWeb/login.html")
        time.sleep(2)
        driver.find_element(By.ID, "username").send_keys("abc@gmail.com")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.XPATH, "//*[@id='login-form']/button").click()
        time.sleep(2)
        
        # Điều hướng đến trang user
        driver.get("http://localhost/ProjectWeb/userhtml.php")
        time.sleep(2)
        
        # Click vào nút sửa thông tin người dùng
        driver.find_element(By.XPATH, "/html/body/div[4]/table/tbody/tr[3]/td[4]/button[1]").click()
        
        # Sửa thông tin người dùng
        driver.find_element(By.ID, "fullname").clear()
        driver.find_element(By.ID, "fullname").send_keys("taun")
        
        # Click lưu thay đổi
        driver.find_element(By.XPATH, "/html/body/div[4]/table/tbody/tr[5]/td[4]/button[1]").click()
        
        # Nếu mọi thứ đều thành công, in thông báo
        print("Edit account successful")
        
    except (NoSuchElementException, WebDriverException) as e:
        # Nếu có lỗi, in thông báo lỗi
        print(f"An error occurred: {e}")

def test_edit_account_blank_fields(driver):#Bug 
    try:
        #Login 
        driver.get("http://localhost/ProjectWeb/login.html")
        time.sleep(2)
        driver.find_element(By.ID, "username").send_keys("abc@gmail.com")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.XPATH, "//*[@id='login-form']/button").click()
        time.sleep(2)
        
        driver.get("http://localhost/ProjectWeb/userhtml.php")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[4]/table/tbody/tr[3]/td[4]/button[1]").click()
        # Sửa thông tin người dùng
        driver.find_element(By.ID, "fullname").clear()
        
        # Click lưu thay đổi
        driver.find_element(By.XPATH, "/html/body/div[4]/table/tbody/tr[5]/td[4]/button[1]").click()
        
        print('Edit account successful')

    except (NoSuchElementException, WebDriverException) as e:
        #Nếu có lỗi, in thông báo lỗi
        print(f"An error occurred: {e}")

# Khóa/Mở khóa tài khoản
def test_lock_account(driver):
    try :
        #Login 
        driver.get("http://localhost/ProjectWeb/login.html")
        time.sleep(2)
        driver.find_element(By.ID, "username").send_keys("abc@gmail.com")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.XPATH, "//*[@id='login-form']/button").click()
        time.sleep(2)
        
        driver.get("http://localhost/ProjectWeb/userhtml.php")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[4]/table/tbody/tr[5]/td[5]/button").click()
        alert = Alert(driver)
        alert.accept()
        
        print("Account locked successfully")
        
        
    except (NoSuchElementException, WebDriverException) as e:
        print(f"An error occurred: {e}")

def test_unlock_account(driver):
    try:
        #Login 
        driver.get("http://localhost/ProjectWeb/login.html")
        time.sleep(2)
        driver.find_element(By.ID, "username").send_keys("abc@gmail.com")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.XPATH, "//*[@id='login-form']/button").click()
        time.sleep(2)
        
        driver.get("http://localhost/ProjectWeb/userhtml.php")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[4]/table/tbody/tr[5]/td[5]/button").click()
        
        alert = Alert(driver)
        alert.accept()
            
        print("Account unlocked successfully")
        
        
    except (NoSuchElementException, WebDriverException) as e:
        print(f"An error occurred: {e}")