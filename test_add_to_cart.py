import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import login as l
@pytest.fixture
def driver():
    # Tự động quản lý ChromeDriver
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

#add 1 product
def test_add_to_cart(driver):
    l.login(driver)
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='boxajax-containter']/section[1]/div/div[1]/div[1]/a/img").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[1]/div/button").click()
    time.sleep(2)
    status=driver.find_element(By.XPATH,"//*[@id='cart-status']").text
    assert status=="Đã thêm vào giỏ hàng","failed to add to cart"

#add 2 or more products
def test_add_multi_to_cart(driver):
    l.login(driver)
    time.sleep(2)
    # Variables
    added_products = 0
    number_product = 5  # Number of products to add
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
    
    # Navigate to the cart and verify items
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/a[3]/img").click()
    time.sleep(2)
    cart_items = driver.find_elements(By.XPATH, "//*[@id='boxajax-containter']/table//div/h3")
    cart_product_names = [item.text for item in cart_items]
    print(f"Products in cart: {cart_product_names}")
    
    # Assert the number of added products matches the cart items
    assert added_products == len(cart_product_names), "Failed to add all products"

def test_add_same_product(driver):
    l.login(driver)
    time.sleep(2)
    name_element = driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/section[1]/div/div[1]/div[2]/h2").text
    product_element = driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/section[1]/div/div[1]/div[1]/a/img")
    product_element.click()
    time.sleep(1)
    add = 2
    for _ in range(add):
        driver.find_element(By.XPATH, "/html/body/section[1]/div/button").click()
        time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/a[3]/img").click()
    time.sleep(2)
    quantity_product = driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/table/tbody/tr[2]/td[2]/input").get_attribute("value")
    quantity_product = int(quantity_product)  # Convert value to integer
    name_product = driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/table/tbody/tr[2]/td[1]/div/div/h3").text
    assert name_element.lower() == name_product.lower(), f"Product names do not match: {name_element} != {name_product}"
    assert quantity_product == add, f"Product quantity mismatch: {quantity_product} != {add}"
    print("Test passed: Same product added successfully with correct quantity.")
