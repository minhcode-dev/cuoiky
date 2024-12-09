import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
@pytest.fixture
def driver():
    # Tự động quản lý ChromeDriver
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_checkout_product_has_added(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("123456789")
    driver.find_element(By.CLASS_NAME,"submit-btn").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/a[3]/img").click()
    sex="Nam"
    driver.find_element(By.XPATH,f"//*[@id='{sex}']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='my-form']/div[1]/a").click()
    time.sleep(2)
    city="HCM"
    street="abc"
    address="113"
    backup_add=""
    driver.find_element(By.XPATH,"/html/body/div/form/div[1]/input[1]").send_keys(city)
    driver.find_element(By.XPATH,"/html/body/div/form/div[1]/input[2]").send_keys(street)
    driver.find_element(By.XPATH,"/html/body/div/form/div[1]/input[3]").send_keys(address)
    driver.find_element(By.XPATH,"/html/body/div/form/div[1]/input[4]").send_keys(backup_add)
    driver.find_element(By.XPATH,"/html/body/div/form/button").click()
    time.sleep(2)
    try:
        select_element=driver.find_element(By.XPATH,"//*[@id='mySelect']")
        select = Select(select_element)
        address="HCM abc 113"
        select.select_by_visible_text(address)
    except:
        print("dont have any address to choose")
    driver.find_element(By.XPATH,"//*[@id='cod']").click()
    phone_number="0123456789"
    driver.find_element(By.XPATH, '//*[@id="sdt"]').send_keys(phone_number)
    driver.find_element(By.XPATH,"//*[@id='billajax']/table/tbody/tr[4]/td[2]/button").click()
    time.sleep(5)
    alert=driver.find_element(By.XPATH,"//*[@id='boxajax']/table/tbody/tr[2]/th[6]/p").text
    assert alert=="Đang Xử Lý","failed to checkout"

def test_checkout_no_inf(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    # Đăng nhập
    driver.find_element(By.XPATH, "//*[@id='user-img']").click()
    driver.find_element(By.XPATH, "//*[@id='user-btn']").click()
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("123456789")
    driver.find_element(By.CLASS_NAME, "submit-btn").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/a[3]/img").click()
    # Nhấn nút để kích hoạt thông báo
    driver.find_element(By.XPATH, "//*[@id='billajax']/table/tbody/tr[4]/td[2]/button").click()
    time.sleep(5)
    # Chờ thông báo xuất hiện
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Nội dung thông báo: {alert_text}")
    assert alert_text == "Vui lòng điền đủ thông tin.", "Thông báo không đúng như mong đợi!"
    alert.accept()

def test_increase_quantity(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH, "//*[@id='user-img']").click()
    driver.find_element(By.XPATH, "//*[@id='user-btn']").click()
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("123456789")
    driver.find_element(By.CLASS_NAME, "submit-btn").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/a[3]/img").click()
    price_bf = driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/table/tbody/tr[2]/td[3]").text
    price_bf = float(price_bf.replace("₫", "").replace(".", "").strip())
    time.sleep(2)
    increase_button=driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/table/tbody/tr[2]/td[2]/button[2]")
    num_click=2
    for _ in range(num_click):
        increase_button.click()
        time.sleep(1)
    price_af = driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/table/tbody/tr[2]/td[3]").text
    price_af = float(price_af.replace("₫", "").replace(".", "").strip())
    expected_price_af = price_bf * (num_click+1)
    assert price_af == expected_price_af, f"Failed to increase: {price_bf} and {expected_price_af}"

def test_decrease_quantity(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH, "//*[@id='user-img']").click()
    driver.find_element(By.XPATH, "//*[@id='user-btn']").click()
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("123456789")
    driver.find_element(By.CLASS_NAME, "submit-btn").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/a[3]/img").click()
    price_bf = driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/table/tbody/tr[2]/td[3]").text
    price_bf = float(price_bf.replace("₫", "").replace(".", "").strip())
    time.sleep(2)
    decrease_button=driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/table/tbody/tr[2]/td[2]/button[1]")
    num_click=2
    for _ in range(num_click):
        decrease_button.click()
        time.sleep(1)
    price_af = driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/table/tbody/tr[2]/td[3]").text
    price_af = float(price_af.replace("₫", "").replace(".", "").strip())
    expected_price_af = price_bf / num_click  # Giả định giá giảm tuyến tính theo số lượng
    assert price_af == expected_price_af, f"Failed to increase: {price_bf} and {expected_price_af}"

