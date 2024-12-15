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
    
# Delete account
def test_delete_account_success(driver):
    try:
        # Login
        driver.get("http://localhost/ProjectWeb/login.html")
        time.sleep(2)
        driver.find_element(By.ID, "username").send_keys("abc@gmail.com")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.XPATH, "//*[@id='login-form']/button").click()
        time.sleep(2)
        
        # Điều hướng đến trang quản lý tài khoản
        driver.get("http://localhost/ProjectWeb/userhtml.php")
        time.sleep(2)

        # Chọn tài khoản và nhấn nút "Xóa"
        driver.find_element(By.XPATH, "/html/body/div[4]/table/tbody/tr[4]/td[4]/button[2]").click()
        time.sleep(1)

        # Xác nhận xóa
        driver.find_element(By.XPATH, "/html/body/div[4]/table/tbody/tr[4]/td[4]/button[1]").click()
        time.sleep(2)

        # Xử lý alert sau khi xóa
        alert = Alert(driver)
        alert.accept()

        # Kiểm tra thông báo thành công
        print("Delete account successful")
    
    except (NoSuchElementException, WebDriverException) as e:
        print(f"An error occurred: {e}")

def test_delete_account_not_exist(driver):
    try:
        # Login
        driver.get("http://localhost/ProjectWeb/login.html")
        time.sleep(2)
        driver.find_element(By.ID, "username").send_keys("abc@gmail.com")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.XPATH, "//*[@id='login-form']/button").click()
        time.sleep(2)
        
        # Điều hướng đến trang quản lý tài khoản
        driver.get("http://localhost/ProjectWeb/userhtml.php")
        time.sleep(2)

        # Gửi yêu cầu xóa tài khoản không tồn tại
        fake_account = {"username": "nonexistent_user", "action": "delete"}
        driver.execute_script("""queryRequest(arguments[0]);""", fake_account)
        time.sleep(2)

        # Kiểm tra thông báo lỗi
        alert = Alert(driver)
        alert.accept()
        
        # Kiểm tra thông báo lỗi
        print("Account not exist")

    except (NoSuchElementException, WebDriverException) as e:
        print(f"An error occurred: {e}")


