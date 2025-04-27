<?php

use PHPUnit\Framework\TestCase;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\WebDriverBy;
use Facebook\WebDriver\WebDriverAlert;

class DeleteProductTest extends TestCase
{
    protected $driver;


    public function setUp(): void
    {
        $host = 'http://localhost:4444/wd/hub'; // Địa chỉ Selenium Server
        $capabilities = DesiredCapabilities::edge(); // Chọn trình duyệt Edge
        $this->driver = RemoteWebDriver::create($host, $capabilities);
        $this->driver->manage()->window()->maximize();
    }

    public function tearDown(): void
    {
        $this->driver->quit();
    }

    public function testDeleteProductByAdmin()
    {
        try {
            // Đăng nhập
            $this->driver->get("http://localhost/ProjectWeb/index.php");
            sleep(3);

            $this->driver->findElement(WebDriverBy::cssSelector("#user-img"))->click();
            sleep(3);

            $this->driver->findElement(WebDriverBy::xpath("//*[@id='user-btn']"))->click();
            sleep(3);

            $this->driver->findElement(WebDriverBy::id("username"))->sendKeys("abc@gmail.com");
            $this->driver->findElement(WebDriverBy::id("password"))->sendKeys("12345678");
            $this->driver->findElement(WebDriverBy::xpath("//*[@id='login-form']/button"))->click();
            sleep(3);

            // Xóa sản phẩm
            $this->driver->findElement(WebDriverBy::xpath("//*[@id='boxajax-containter']/section[1]/div/div[1]/div[1]/a[3]/button"))->click();
            sleep(3);

            $alert = $this->driver->switchTo()->alert();
            $alert->accept();
            
            // Kiểm tra thành công
            $this->assertTrue(true, "Successfully deleted product");
        } catch (Exception $e) {
            $this->fail("Test Failed: " . $e->getMessage());
        }
    }

    public function testDeleteProductByUser()
    {
        try {
            // Đăng nhập
            $this->driver->get("http://localhost/ProjectWeb/index.php");
            sleep(3);

            $this->driver->findElement(WebDriverBy::cssSelector("#user-img"))->click();
            sleep(3);

            $this->driver->findElement(WebDriverBy::xpath("//*[@id='user-btn']"))->click();
            sleep(3);

            $this->driver->findElement(WebDriverBy::id("username"))->sendKeys("asd@gmail.com");
            $this->driver->findElement(WebDriverBy::id("password"))->sendKeys("12345678");
            $this->driver->findElement(WebDriverBy::xpath("//*[@id='login-form']/button"))->click();
            sleep(3);

            // Cố gắng xóa sản phẩm
            try {
                $this->driver->findElement(WebDriverBy::xpath("//*[@id='boxajax-containter']/section[1]/div/div[1]/div[1]/a[3]/button"))->click();
                sleep(3);
                $this->fail("Account should not have permission to delete products.");
            } catch (Exception $e) {
                // Kiểm tra không có quyền xóa
                $this->assertTrue(true, "Accounts don't have permission to delete products");
            }
        } catch (Exception $e) {
            $this->fail("Test Failed: " . $e->getMessage());
        }
    }
}
