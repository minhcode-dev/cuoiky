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


def test_brand_filter(driver):
    l.login(driver)
    time.sleep(2)
    dropdown = driver.find_element(By.XPATH, "//*[@id='select-brand']")
    select = Select(dropdown)
    brand="MSI"
    select.select_by_visible_text(brand)
    driver.find_element(By.XPATH, "//*[@id='select-brand']").click()
    time.sleep(2)
    product_elements = driver.find_elements(By.XPATH, "//div[@class='product-card']//h2")
    product_brands = [product.text.lower() for product in product_elements]
    print(product_brands)
    assert all(f"{brand.lower()}" in product for product in product_brands)
    print(f"products belong to {brand}:", product_brands)


def test_filter_range_prices(driver):
    l.login(driver)
    time.sleep(2)
    dropdown = driver.find_element(By.XPATH, "//*[@id='select-cost']")
    select = Select(dropdown)
    price_range="từ 5 tới 15 triệu"
    select.select_by_visible_text(price_range)
    driver.find_element(By.XPATH, "//*[@id='select-cost']").click()
    time.sleep(2)
    product_price_elements = driver.find_elements(By.XPATH, "//div[@class='product-card']//span[@class='price']")
    product_prices = []
    for product in product_price_elements:
        price_text = product.text.lower().replace("usd", "").replace(".", "").strip()
        product_prices.append(price_text)
    max_price=15000000
    min_price=5000000
    assert all(min_price<int(price) <= max_price for price in product_prices),f"some products exceed the price range {price_range}:{product_prices}"
    print(product_prices)

def test_filter_price(driver):
    l.login(driver)
    time.sleep(2)
    dropdown = driver.find_element(By.XPATH, "//*[@id='select-sort']")
    select = Select(dropdown)
    price_range="Giá từ cao đến thấp"
    select.select_by_visible_text(price_range)
    driver.find_element(By.XPATH, "//*[@id='select-sort']").click()
    time.sleep(2)
    product_price_elements = driver.find_elements(By.XPATH, "//div[@class='product-card']//span[@class='price']")
    product_prices = []
    for product in product_price_elements:
        price_text = product.text.lower().replace("usd", "").replace(".", "").strip()
        product_prices.append(price_text)
    for i in range(len(product_prices) - 1):
        assert float(product_prices[i]) >= float(product_prices[i + 1]), \
        f"Prices are not sorted correctly at index {i}: {product_prices[i]} < {product_prices[i + 1]}"

    
