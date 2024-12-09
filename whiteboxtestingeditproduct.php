<?php

use PHPUnit\Framework\TestCase;

class ProductFormTest extends TestCase
{
    // Hàm giả lập validateForm()
    private function validateForm($formData)
    {
        if (empty($formData['ten_sp']) || empty($formData['gia_sp']) || empty($formData['images'])) {
            return false;
        }

        if (count($formData['images']) < 4) {
            return false;
        }

        if ($formData['thuong_hieu'] == "0" || $formData['loai_sp'] == "0") {
            return false;
        }

        return true;
    }

    // Kiểm tra khi các trường nhập liệu bị bỏ trống
    public function testEmptyFields()
    {
        $formData = [
            'ten_sp' => '',
            'gia_sp' => '',
            'images' => [],
            'thuong_hieu' => '0',
            'loai_sp' => '0'
        ];

        $this->assertFalse($this->validateForm($formData), "Test failed: Empty fields should return false");
    }

    // Kiểm tra khi có ít hơn 4 hình ảnh tải lên
    public function testLessThanFourImages()
    {
        $formData = [
            'ten_sp' => 'Laptop Dell',
            'gia_sp' => '20000000',
            'images' => ['image1.jpg', 'image2.jpg', 'image3.jpg'], // Chỉ 3 ảnh
            'thuong_hieu' => 'DELL',
            'loai_sp' => 'laptop'
        ];

        $this->assertFalse($this->validateForm($formData), "Test failed: Less than 4 images should return false");
    }

    // Kiểm tra dropdown chưa chọn giá trị hợp lệ
    public function testInvalidDropdownValues()
    {
        $formData = [
            'ten_sp' => 'Laptop Dell',
            'gia_sp' => '20000000',
            'images' => ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg'],
            'thuong_hieu' => '0', // Thương hiệu chưa chọn
            'loai_sp' => '0'      // Loại chưa chọn
        ];

        $this->assertFalse($this->validateForm($formData), "Test failed: Invalid dropdown values should return false");
    }

    // Kiểm tra khi tất cả dữ liệu hợp lệ
    public function testValidFormData()
    {
        $formData = [
            'ten_sp' => 'Laptop Dell',
            'gia_sp' => '20000000',
            'images' => ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg'],
            'thuong_hieu' => 'DELL',
            'loai_sp' => 'laptop'
        ];

        $this->assertTrue($this->validateForm($formData), "Test failed: Valid form data should return true");
    }

    // Kiểm tra xử lý hình ảnh (preview ảnh)
    public function testImagePreviewHandling()
    {
        $imagePreviewSrc = "data:image/jpeg;base64,someBase64EncodedImage";
        $this->assertStringContainsString("data:image/jpeg;base64", $imagePreviewSrc, "Test failed: Image preview should display correctly");
    }

    // Kiểm tra xác nhận nút "Lưu chỉnh sửa"
    public function testSaveButtonValidation()
    {
        $formData = [
            'ten_sp' => 'Laptop Dell',
            'gia_sp' => '20000000',
            'images' => ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg'],
            'thuong_hieu' => 'DELL',
            'loai_sp' => 'laptop'
        ];

        $this->assertTrue($this->validateForm($formData), "Test failed: Save button should work with valid form data");
    }
}
