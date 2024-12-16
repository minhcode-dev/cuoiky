<?php
use PHPUnit\Framework\TestCase;

class RegisterFormTest extends TestCase
{
    private $form;

    protected function setUp(): void
    {
        // Mô phỏng hành vi của form "Đăng ký"
        $this->form = new RegisterForm();
    }

    public function testEmptyFields()
    {
        $result = $this->form->validate(
            '', // Họ tên
            '', // Email
            '', // Tên tài khoản
            '', // Mật khẩu
            false // Đồng ý điều khoản
        );
        $this->assertFalse($result);
        $this->assertEquals('Các trường không được để trống.', $this->form->getErrorMessage());
    }

    public function testInvalidEmail()
    {
        $result = $this->form->validate(
            'Nguyen Van A',
            'invalid-email',
            'username',
            'password123',
            true
        );
        $this->assertFalse($result);
        $this->assertEquals('Email không hợp lệ.', $this->form->getErrorMessage());
    }

    public function testPasswordTooShort()
    {
        $result = $this->form->validate(
            'Nguyen Van A',
            'example@example.com',
            'username',
            '123', // Mật khẩu quá ngắn
            true
        );
        $this->assertFalse($result);
        $this->assertEquals('Mật khẩu phải có ít nhất 6 ký tự.', $this->form->getErrorMessage());
    }

    public function testMissingAgreement()
    {
        $result = $this->form->validate(
            'Nguyen Van A',
            'example@example.com',
            'username',
            'password123',
            false // Không đồng ý điều khoản
        );
        $this->assertFalse($result);
        $this->assertEquals('Bạn phải đồng ý với điều khoản và chính sách bảo mật.', $this->form->getErrorMessage());
    }

    public function testSuccessfulRegistration()
    {
        $result = $this->form->validate(
            'Nguyen Van A',
            'example@example.com',
            'username',
            'password123',
            true
        );
        $this->assertTrue($result);
    }
}

class RegisterForm
{
    private $errorMessage;

    public function validate($hoten, $email, $username, $password, $agreeTerms)
    {
        if (empty($hoten) || empty($email) || empty($username) || empty($password)) {
            $this->errorMessage = 'Các trường không được để trống.';
            return false;
        }

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $this->errorMessage = 'Email không hợp lệ.';
            return false;
        }

        if (strlen($password) < 6) {
            $this->errorMessage = 'Mật khẩu phải có ít nhất 6 ký tự.';
            return false;
        }

        if (!$agreeTerms) {
            $this->errorMessage = 'Bạn phải đồng ý với điều khoản và chính sách bảo mật.';
            return false;
        }

        return true;
    }

    public function getErrorMessage()
    {
        return $this->errorMessage;
    }
}
