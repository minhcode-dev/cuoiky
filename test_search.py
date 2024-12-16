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

def test_search_case_sensitive(driver):
    l.login(driver)
    search_input = "acer"
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/input").send_keys(search_input)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/button").click()
    time.sleep(5)
    # Get all product names
    product_elements = driver.find_elements(By.XPATH, "/html/body/section/div[3]//h2")
    p_name = [product.text.lower() for product in product_elements]
    print("Products found:", p_name)
    # Assert if any product contains the search input
    assert any(search_input.lower() in product for product in p_name), f"No products match '{search_input}'"

def test_search_exact_product_name(driver):
    l.login(driver)
    search_input = "ACER NITRO GAMING 5"
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/input").send_keys(search_input)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/button").click()
    time.sleep(5)
    # Get all product names
    product_elements = driver.find_elements(By.XPATH, "/html/body/section/div[3]//h2")
    p_name = [product.text.lower() for product in product_elements]
    print("Products found:", p_name)
    # Assert if any product contains the search input
    assert any(search_input.lower() in product for product in p_name), f"No products match '{search_input}'"

# Test case for search with leading/trailing space
def test_search_space(driver):
    l.login(driver)
    search_input = " Acer"  # Leading space
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/input").send_keys(search_input)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/button").click()
    time.sleep(5)
    # Get all product names
    product_elements = driver.find_elements(By.XPATH, "/html/body/section/div[3]//h2")
    p_name = [product.text.lower() for product in product_elements]
    print("Products found:", p_name)
    # Assert if any product contains the search input
    assert any(search_input.strip().lower() in product for product in p_name), f"No products match '{search_input.strip()}'"

# Test case for search with no results
def test_search_no_results(driver):
    l.login(driver)
    search_input = "NonExistingProduct"
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/input").send_keys(search_input)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/button").click()
    time.sleep(5)
    # Get all product names
    product_elements = driver.find_elements(By.XPATH, "/html/body/section/div[3]//h2")
    p_name = [product.text.lower() for product in product_elements]
    print("Products found:", p_name)
    # Assert that no products are found
    assert not any(search_input.lower() in product for product in p_name), f"Found products for '{search_input}', but expected no results."

# Test case for empty search input
def test_search_empty_input(driver):
    l.login(driver)
    search_input = ""  # Empty input
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/input").send_keys(search_input)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/button").click()
    time.sleep(5)
    # Get all product names
    product_elements = driver.find_elements(By.XPATH, "/html/body/section/div[3]//h2")
    p_name = [product.text.lower() for product in product_elements]
    print("Products found:", p_name)
    assert len(p_name) > 0, "No products found for empty search input."

# Test case for partial match search
def test_search_partial_match(driver):
    l.login(driver)
    search_input = "le"  # Partial search term
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/input").send_keys(search_input)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/button").click()
    time.sleep(5)
    product_elements = driver.find_elements(By.XPATH, "/html/body/section/div[3]//h2")
    p_name = [product.text.lower() for product in product_elements]
    # Assert if any product partially matches the search input
    assert any(search_input.lower() in product for product in p_name), f"No products partially match '{search_input}'"

def test_search_special_character(driver):
    l.login(driver)
    search_input = "ACER@"
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/input").send_keys(search_input)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/button").click()
    time.sleep(5)
    # Get all product names
    product_elements = driver.find_elements(By.XPATH, "/html/body/section/div[3]//h2")
    p_name = [product.text.lower() for product in product_elements]
    print("Products found:", p_name)
    assert not any(search_input.lower() in product for product in p_name), f"products match '{search_input}'"


