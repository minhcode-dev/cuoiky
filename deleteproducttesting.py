import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import pytest
import mysql.connector

#Connect to database

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",       
            user="root",            
            password="",            
            database="laptrinhweb2" 
        )
        print("Connection to database successful!")
        return conn
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None

@pytest.fixture
def driver():
    
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    
def test_deleteproduct_by_admin(driver):
    
    try: 

        #Login
        driver.get("http://localhost/ProjectWeb/index.php")
        time.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#user-img").click()
        time.sleep(3)
        
        driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
        time.sleep(3)
        
        driver.find_element(By.ID, "username").send_keys("abc@gmail.com")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.XPATH, "//*[@id='login-form']/button").click()
        time.sleep(3)   

        #Delete product
        driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/section[1]/div/div[1]/div[1]/a[3]/button").click()
        time.sleep(3)  
        
        alert = Alert(driver)  
        alert.accept()
        assert "Successfully deleted product"
        
    
        
    except Exception as e:
        print(f"Test Failed: {e}")
        assert False  
    
    finally:
        driver.quit()
        
def test_deleteproduct_by_user(driver):
    try: 
        #Login
        driver.get("http://localhost/ProjectWeb/index.php")
        time.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#user-img").click()
        time.sleep(3)
        
        driver.find_element(By.XPATH,"//*[@id='user-btn']").click()
        time.sleep(3)
        
        driver.find_element(By.ID, "username").send_keys("asd@gmail.com")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.XPATH, "//*[@id='login-form']/button").click()
        time.sleep(3)   

        #Delete product
        try: 
            driver.find_element(By.XPATH, "//*[@id='boxajax-containter']/section[1]/div/div[1]/div[1]/a[3]/button").click()
            time.sleep(3)  
        except:
            assert "Accounts don't have permission to delete products"
        
    except Exception as e:
        print(f"Test Failed: {e}")
        assert False
    finally:
        driver.quit()
    
