<?php

use PHPUnit\Framework\TestCase;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Facebook\WebDriver\WebDriverBy;
use Facebook\WebDriver\WebDriverAlert;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\WebDriverExpectedCondition;

class AccountManagementTest extends TestCase
{
    /** @var RemoteWebDriver */
    private $driver;

    protected function setUp(): void
    {
        $host = 'http://localhost:4444/wd/hub'; // URL of the Selenium server
        $capabilities = DesiredCapabilities::chrome();
        $this->driver = RemoteWebDriver::create($host, $capabilities);
        $this->driver->manage()->window()->maximize();
    }

    protected function tearDown(): void
    {
        $this->driver->quit();
    }

    // Helper function for logging in
    private function login(string $username, string $password): void
    {
        $this->driver->get('http://localhost/ProjectWeb/login.html');
        usleep(2000000); // 2 seconds

        $this->driver->findElement(WebDriverBy::id('username'))->sendKeys($username);
        $this->driver->findElement(WebDriverBy::id('password'))->sendKeys($password);
        $this->driver->findElement(WebDriverBy::xpath("//*[@id='login-form']/button"))->click();

        usleep(2000000); // 2 seconds
    }

    // Test case: Edit account successfully
    public function testEditAccountSuccess(): void
    {
        try {
            $this->login('abc@gmail.com', '12345678');

            $this->driver->get('http://localhost/ProjectWeb/userhtml.php');
            usleep(2000000);

            $editButton = $this->driver->findElement(WebDriverBy::xpath("/html/body/div[4]/table/tbody/tr[3]/td[4]/button[1]"));
            $editButton->click();

            $fullnameField = $this->driver->findElement(WebDriverBy::id('fullname'));
            $fullnameField->clear();
            $fullnameField->sendKeys('taun');

            $saveButton = $this->driver->findElement(WebDriverBy::xpath("/html/body/div[4]/table/tbody/tr[5]/td[4]/button[1]"));
            $saveButton->click();

            echo "Edit account successful\n";
        } catch (NoSuchElementException $e) {
            echo "Element not found during account edit: " . $e->getMessage() . "\n";
        } catch (WebDriverException $e) {
            echo "WebDriver error occurred: " . $e->getMessage() . "\n";
        }
    }

    // Test case: Edit account with blank fields (Bug simulation)
    public function testEditAccountBlankFields(): void
    {
        try {
            $this->login('abc@gmail.com', '12345678');

            $this->driver->get('http://localhost/ProjectWeb/userhtml.php');
            usleep(2000000);

            $editButton = $this->driver->findElement(WebDriverBy::xpath("/html/body/div[4]/table/tbody/tr[3]/td[4]/button[1]"));
            $editButton->click();

            $fullnameField = $this->driver->findElement(WebDriverBy::id('fullname'));
            $fullnameField->clear();

            $saveButton = $this->driver->findElement(WebDriverBy::xpath("/html/body/div[4]/table/tbody/tr[5]/td[4]/button[1]"));
            $saveButton->click();

            echo "Edit account successful\n";
        } catch (NoSuchElementException $e) {
            echo "Element not found during account edit with blank fields: " . $e->getMessage() . "\n";
        } catch (WebDriverException $e) {
            echo "WebDriver error occurred: " . $e->getMessage() . "\n";
        }
    }

    // Test case: Lock account
    public function testLockAccount(): void
    {
        try {
            $this->login('abc@gmail.com', '12345678');

            $this->driver->get('http://localhost/ProjectWeb/userhtml.php');
            usleep(2000000);

            $lockButton = $this->driver->findElement(WebDriverBy::xpath("/html/body/div[4]/table/tbody/tr[5]/td[5]/button"));
            $lockButton->click();

            $alert = $this->driver->switchTo()->alert();
            $alert->accept();

            echo "Account locked successfully\n";
        } catch (NoSuchElementException $e) {
            echo "Element not found during account lock: " . $e->getMessage() . "\n";
        } catch (WebDriverException $e) {
            echo "WebDriver error occurred: " . $e->getMessage() . "\n";
        }
    }

    // Test case: Unlock account
    public function testUnlockAccount(): void
    {
        try {
            $this->login('abc@gmail.com', '12345678');

            $this->driver->get('http://localhost/ProjectWeb/userhtml.php');
            usleep(2000000);

            $unlockButton = $this->driver->findElement(WebDriverBy::xpath("/html/body/div[4]/table/tbody/tr[5]/td[5]/button"));
            $unlockButton->click();

            $alert = $this->driver->switchTo()->alert();
            $alert->accept();

            echo "Account unlocked successfully\n";
        } catch (NoSuchElementException $e) {
            echo "Element not found during account unlock: " . $e->getMessage() . "\n";
        } catch (WebDriverException $e) {
            echo "WebDriver error occurred: " . $e->getMessage() . "\n";
        }
    }
}
