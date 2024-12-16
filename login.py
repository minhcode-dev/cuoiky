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

def login(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH, "//*[@id='user-img']").click()
    driver.find_element(By.XPATH, "//*[@id='user-btn']").click()
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("123456789")
    driver.find_element(By.CLASS_NAME, "submit-btn").click()

def login_wrong_pass(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH, "//*[@id='user-img']").click()
    driver.find_element(By.XPATH, "//*[@id='user-btn']").click()
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("123456")
    driver.find_element(By.CLASS_NAME, "submit-btn").click()

def login_blank_pass(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH, "//*[@id='user-img']").click()
    driver.find_element(By.XPATH, "//*[@id='user-btn']").click()
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tester111")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("")
    driver.find_element(By.CLASS_NAME, "submit-btn").click()

def login_wrong_user(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH, "//*[@id='user-img']").click()
    driver.find_element(By.XPATH, "//*[@id='user-btn']").click()
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tester")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("123456789")
    driver.find_element(By.CLASS_NAME, "submit-btn").click()

def login_blank_user(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH, "//*[@id='user-img']").click()
    driver.find_element(By.XPATH, "//*[@id='user-btn']").click()
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("123456789")
    driver.find_element(By.CLASS_NAME, "submit-btn").click()

def login_blank_all(driver):
    driver.get("http://localhost/ProjectWeb/index.php")
    driver.find_element(By.XPATH, "//*[@id='user-img']").click()
    driver.find_element(By.XPATH, "//*[@id='user-btn']").click()
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("")
    driver.find_element(By.CLASS_NAME, "submit-btn").click()