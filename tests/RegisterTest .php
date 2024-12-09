
<?php
use PHPUnit\Framework\TestCase;

class RegisterTest extends TestCase
{
    private $mockDbConnection;

    protected function setUp(): void
    {
        $this->mockDbConnection = $this->createMock(mysqli::class);
    }

    public function testSuccessfulRegistration()
    {
        // Dữ liệu người dùng nhập vào
        $_POST['hoten'] = 'Test User';
        $_POST['email'] = 'test@gmail.com';
        $_POST['username'] = 'testuser';
        $_POST['password'] = '123456789';
        $_REQUEST['submitDangky'] = true;

        $hashedPassword = password_hash($_POST['password'], PASSWORD_DEFAULT);

        $this->mockDbConnection->method('query')->willReturn(true);

        ob_start();
        include 'C:\xampp\htdocs\ProjectWeb\xulySigup.php';
        $output = ob_get_clean();
        $this->assertStringContainsString("Location: login.html", xdebug_get_headers());
    }

    public function testMissingFields()
    {
        $_POST['hoten'] = '';
        $_POST['email'] = 'test@gmail.com';
        $_POST['username'] = 'testuser1';
        $_POST['password'] = '123456789';
        $_REQUEST['submitDangky'] = true;

        ob_start();
        include 'C:\xampp\htdocs\ProjectWeb\xulySigup.php';
        $output = ob_get_clean();
        $this->assertStringContainsString("Error", $output);
    }

    public function testDatabaseError()
    {
        $_POST['hoten'] = 'Test User';
        $_POST['email'] = 'test@gmail.com';
        $_POST['username'] = 'testuser2';
        $_POST['password'] = '123456789';
        $_REQUEST['submitDangky'] = true;

        $this->mockDbConnection->method('query')->willReturn(false);

        ob_start();
        include 'C:\xampp\htdocs\ProjectWeb\xulySigup.php';
        $output = ob_get_clean();
        $this->assertStringContainsString("Error: ", $output);
    }

    public function testInvalidEmail()
    {
        // Dữ liệu người dùng với email không hợp lệ
        $_POST['hoten'] = 'Test User';
        $_POST['email'] = 'invalid-email';
        $_POST['username'] = 'testuser3';
        $_POST['password'] = 'securepassword';
        $_REQUEST['submitDangky'] = true;

        ob_start();
        include 'C:\xampp\htdocs\ProjectWeb\xulySigup.php';
        $output = ob_get_clean();
        $this->assertStringContainsString("Invalid email format", $output);
    }

    public function testShortPassword()
    {
        $_POST['hoten'] = 'Test User';
        $_POST['email'] = 'test@example.com';
        $_POST['username'] = 'testuser';
        $_POST['password'] = '12345';
        $_REQUEST['submitDangky'] = true;

        ob_start();
        include 'C:\xampp\htdocs\ProjectWeb\xulySigup.php';
        $output = ob_get_clean();
        $this->assertStringContainsString("Mật Khẩu Phải Có íT Nhất 8 Kí Tự", $output);
    }

    public function testDuplicateUsername()
    {
        $_POST['hoten'] = 'Test User';
        $_POST['email'] = 'test@example.com';
        $_POST['username'] = 'tester111'; // Username đã tồn tại
        $_POST['password'] = '123456789';
        $_REQUEST['submitDangky'] = true;

        $this->mockDbConnection->method('query')->willReturn(false);

        ob_start();
        include 'C:\xampp\htdocs\ProjectWeb\xulySigup.php';
        $output = ob_get_clean();
        $this->assertStringContainsString("Username already exists", $output);
    }
}
?>
