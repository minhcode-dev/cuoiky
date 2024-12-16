<?php

use PHPUnit\Framework\TestCase;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Facebook\WebDriver\WebDriverBy;
use Facebook\WebDriver\WebDriverAlert;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\WebDriverExpectedCondition;

class AccountDeletionTest extends TestCase
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

    // Test case: Delete account successfully
    public function testDeleteAccountSuccess(): void
    {
        try {
            // Step 1: Login with valid credentials
            $this->login('abc@gmail.com', '12345678');

            // Step 2: Navigate to user management page
            $this->driver->get('http://localhost/ProjectWeb/userhtml.php');
            usleep(2000000); // 2 seconds

            // Step 3: Attempt to delete an existing account
            $deleteButton = $this->driver->findElement(WebDriverBy::xpath("/html/body/div[4]/table/tbody/tr[4]/td[4]/button[2]"));
            $deleteButton->click();
            usleep(1000000); // 1 second

            $confirmButton = $this->driver->findElement(WebDriverBy::xpath("/html/body/div[4]/table/tbody/tr[4]/td[4]/button[1]"));
            $confirmButton->click();
            usleep(2000000); // 2 seconds

            // Step 4: Handle alert confirmation
            $alert = $this->driver->switchTo()->alert();
            $alert->accept();

            echo "Delete account successful\n";
        } catch (NoSuchElementException $e) {
            echo "Element not found during account deletion: " . $e->getMessage() . "\n";
        } catch (WebDriverException $e) {
            echo "WebDriver error occurred: " . $e->getMessage() . "\n";
        }
    }

    // Test case: Attempt to delete a non-existent account
    public function testDeleteAccountNotExist(): void
    {
        try {
            // Step 1: Login with valid credentials
            $this->login('abc@gmail.com', '12345678');

            // Step 2: Navigate to user management page
            $this->driver->get('http://localhost/ProjectWeb/userhtml.php');
            usleep(2000000); // 2 seconds

            // Step 3: Simulate deleting a non-existent account via script
            $fakeAccount = json_encode(["username" => "nonexistent_user", "action" => "delete"]);
            $this->driver->executeScript("queryRequest(arguments[0]);", [$fakeAccount]);
            usleep(2000000); // 2 seconds

            // Step 4: Handle alert confirmation
            $alert = $this->driver->switchTo()->alert();
            $alert->accept();

            echo "Account does not exist\n";
        } catch (NoSuchElementException $e) {
            echo "Element not found during non-existent account deletion: " . $e->getMessage() . "\n";
        } catch (WebDriverException $e) {
            echo "WebDriver error occurred: " . $e->getMessage() . "\n";
        }
    }
}
