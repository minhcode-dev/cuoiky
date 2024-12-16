import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import re
import login as l
@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

#product is added
def test_checkout_cod(driver):
    l.login(driver)
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
     #price
    price_bf=driver.find_element(By.XPATH,"//*[@id='myTD1']").text
    print(price_bf)
    driver.find_element(By.XPATH,"//*[@id='billajax']/table/tbody/tr[4]/td[2]/button").click()
    time.sleep(5)
    expected_id="#62"
    driver.find_element(By.XPATH,"/html/body/div[1]/div/a[2]/img").click()
    time.sleep(2)
    order_history=driver.find_element(By.XPATH,"//*[@id='boxajax']").text
    price_history = re.findall(r"\d[\d.,]*₫", order_history)
    price_history_cleaned = [price.replace("₫", "") for price in price_history]

    order_ids = re.findall(r"#\d+", order_history)    
    if order_ids:
        last_order_id = order_ids[-1]
        last_price=price_history_cleaned[-1]
        print(last_price)
        print(last_order_id)
        assert last_order_id == expected_id and last_price == price_bf , f"Expected ID and price: {expected_id},{price_bf}, but got: {last_order_id},{last_price}"
    else:
        raise AssertionError("No orders found in order history")

def test_checkout_onl(driver):
    l.login(driver)
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
    driver.find_element(By.XPATH,"//*[@id='onl']").click()
    driver.find_element(By.XPATH,"//*[@id='bank']").send_keys("0123456789")
    phone_number="0123456789"
    driver.find_element(By.XPATH, '//*[@id="sdt"]').send_keys(phone_number)
    driver.find_element(By.XPATH,"//*[@id='billajax']/table/tbody/tr[4]/td[2]/button").click()
    expected_id="#50"
    driver.find_element(By.XPATH,"/html/body/div[1]/div/a[2]/img").click()
    time.sleep(2)
    order_history=driver.find_element(By.XPATH,"//*[@id='boxajax']").text
    order_ids = re.findall(r"#\d+", order_history)    
    if order_ids:
        last_order_id = order_ids[-1]
        print(last_order_id)
        assert last_order_id == expected_id, f"Expected ID: {expected_id}, but got: {last_order_id}"
    else:
        raise AssertionError("No orders found in order history")


#cant checkout when the cart is empty
def test_checkout_empty(driver):
    l.login(driver)
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/a[3]/img").click()
    order_button=driver.find_element(By.XPATH,"//*[@id='billajax']/table/tbody/tr[4]/td[2]/button")
    assert not order_button.is_displayed(), "Place Order button is visible"

def test_checkout_product(driver):
    l.login(driver)
    added_products = 0
    number_product = 2  # Number of products to add
    container_xpath = "//*[@id='boxajax-containter']/section[1]/div"
    scrollable_container = driver.find_element(By.XPATH, container_xpath)
    for i in range(number_product):
        try:
            # Locate product element
            product_xpath = f"{container_xpath}/div[{i + 1}]/div[1]/a/img"
            product_element = driver.find_element(By.XPATH, product_xpath)
            # Scroll product into view
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", product_element)
            time.sleep(1)
            
            # Click on product and add to cart
            product_element.click()
            time.sleep(1)
            driver.find_element(By.XPATH, "/html/body/section[1]/div/button").click()
            time.sleep(2)
            
            # Go back to the product list
            driver.back()
            time.sleep(1)
            added_products += 1
        except Exception as e:
            print(f"Error adding product {i + 1}: {e}")
            
            # Scroll container to try loading more products
            driver.execute_script("arguments[0].scrollLeft += 300;", scrollable_container)
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
    expected_id="#50"
    driver.find_element(By.XPATH,"/html/body/div[1]/div/a[2]/img").click()
    time.sleep(2)
    order_history=driver.find_element(By.XPATH,"//*[@id='boxajax']").text
    order_ids = re.findall(r"#\d+", order_history)    
    if order_ids:
        last_order_id = order_ids[-1]
        print(last_order_id)
        assert last_order_id == expected_id, f"Expected ID: {expected_id}, but got: {last_order_id}"
    else:
        raise AssertionError("No orders found in order history")

def test_checkout_no_inf(driver):
    l.login(driver)
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/a[3]/img").click()
    driver.find_element(By.XPATH, "//*[@id='billajax']/table/tbody/tr[4]/td[2]/button").click()
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Nội dung thông báo: {alert_text}")
    assert alert_text == "Vui lòng điền đủ thông tin.", "Thông báo không đúng như mong đợi!"
    alert.accept()

def test_increase_quantity(driver):
    l.login(driver)
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
    l.login(driver)
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
    expected_price_af = price_bf / num_click
    assert price_af == expected_price_af, f"Failed to decrease: {price_bf} and {expected_price_af}"
