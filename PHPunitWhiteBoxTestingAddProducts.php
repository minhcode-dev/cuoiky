<?php
use PHPUnit\Framework\TestCase;

class ProductValidationTest extends TestCase
{
    public function testValidateFormValidInput()
    {
        // Dữ liệu hợp lệ
        $ten_sp = "Laptop Acer";
        $ma_sp = "ACER123";
        $mota_sp = "Máy tính xách tay Acer chính hãng.";
        $filetoup = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg'];
        $gia_sp = 15000000;
        $stock = 30;
        $thuong_hieu = "ACER";
        $loai_sp = "Laptop";

        $result = validateForm($ten_sp, $ma_sp, $mota_sp, $filetoup, $gia_sp, $stock, $thuong_hieu, $loai_sp);
        $this->assertTrue($result); // Kỳ vọng hàm trả về true
    }

    public function testValidateFormMissingProductName()
    {
        // Thiếu tên sản phẩm
        $ten_sp = "";
        $ma_sp = "ACER123";
        $mota_sp = "Máy tính xách tay Acer chính hãng.";
        $filetoup = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg'];
        $gia_sp = 15000000;
        $stock = 30;
        $thuong_hieu = "ACER";
        $loai_sp = "Laptop";

        $result = validateForm($ten_sp, $ma_sp, $mota_sp, $filetoup, $gia_sp, $stock, $thuong_hieu, $loai_sp);
        $this->assertFalse($result); // Kỳ vọng hàm trả về false
    }

    public function testValidateFormInvalidStock()
    {
        // Số lượng trong kho không hợp lệ (ít hơn 20)
        $ten_sp = "Laptop Acer";
        $ma_sp = "ACER123";
        $mota_sp = "Máy tính xách tay Acer chính hãng.";
        $filetoup = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg'];
        $gia_sp = 15000000;
        $stock = 10; // Khoảng 10 không hợp lệ
        $thuong_hieu = "ACER";
        $loai_sp = "Laptop";

        $result = validateForm($ten_sp, $ma_sp, $mota_sp, $filetoup, $gia_sp, $stock, $thuong_hieu, $loai_sp);
        $this->assertFalse($result); // Kỳ vọng hàm trả về false
    }

    public function testValidateFormMissingImages()
    {
        // Thiếu ảnh
        $ten_sp = "Laptop Acer";
        $ma_sp = "ACER123";
        $mota_sp = "Máy tính xách tay Acer chính hãng.";
        $filetoup = ['image1.jpg', 'image2.jpg']; // Thiếu 2 ảnh
        $gia_sp = 15000000;
        $stock = 30;
        $thuong_hieu = "ACER";
        $loai_sp = "Laptop";

        $result = validateForm($ten_sp, $ma_sp, $mota_sp, $filetoup, $gia_sp, $stock, $thuong_hieu, $loai_sp);
        $this->assertFalse($result); // Kỳ vọng hàm trả về false
    }

    public function testValidateFormEmptyPrice()
    {
        // Thiếu giá sản phẩm
        $ten_sp = "Laptop Acer";
        $ma_sp = "ACER123";
        $mota_sp = "Máy tính xách tay Acer chính hãng.";
        $filetoup = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg'];
        $gia_sp = ""; // Giá sản phẩm trống
        $stock = 30;
        $thuong_hieu = "ACER";
        $loai_sp = "Laptop";

        $result = validateForm($ten_sp, $ma_sp, $mota_sp, $filetoup, $gia_sp, $stock, $thuong_hieu, $loai_sp);
        $this->assertFalse($result); // Kỳ vọng hàm trả về false
    }
}
?>
