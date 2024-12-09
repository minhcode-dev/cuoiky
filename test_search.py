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

#test search
def test_search(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH,"//*[@id='user-img']").click()
    driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("123456789")
    driver.find_element(By.CLASS_NAME,"submit-btn").click()
    time.sleep(2)
    search_input="Acer@"
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/input").send_keys(search_input)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/button").click()
    time.sleep(5)
    product_elements = driver.find_elements(By.XPATH, "/html/body/section/div[3]//h2")
    p_name=[product.text.lower() for product in product_elements]
    print("Products found:", p_name)
    assert any(search_input in product for product in p_name), f"No products match '{search_input}'."
