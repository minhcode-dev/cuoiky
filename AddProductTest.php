<?php
use PHPUnit\Framework\TestCase;

class AddProductTest extends TestCase
{
    private $testProductData;

    protected function setUp(): void
    {
        // Khởi tạo dữ liệu mẫu để kiểm thử
        $this->testProductData = [
            'ten_sp' => 'Laptop DELL Inspiron',
            'ma_sp' => 'DELL12345',
            'mota_sp' => 'Mô tả sản phẩm chi tiết.',
            'gia_sp' => 15000000,
            'thuong_hieu' => 'DELL',
            'loai_sp' => 'laptop',
            'stock' => 50,
            'filetoup' => [
                __DIR__ . '/test_image1.jpg',
                __DIR__ . '/test_image2.jpg',
                __DIR__ . '/test_image3.jpg',
                __DIR__ . '/test_image4.jpg'
            ]
        ];

        foreach ($this->testProductData['filetoup'] as $file) {
            file_put_contents($file, 'dummy content'); // Tạo file ảnh tạm thời
        }
    }

    protected function tearDown(): void
    {
        // Xóa các file tạm sau khi kiểm thử
        foreach ($this->testProductData['filetoup'] as $file) {
            if (file_exists($file)) {
                unlink($file);
            }
        }
    }

    public function testValidProductData(): void
    {
        // Kiểm tra dữ liệu hợp lệ
        $_POST = [
            'ten_sp' => $this->testProductData['ten_sp'],
            'ma_sp' => $this->testProductData['ma_sp'],
            'mota_sp' => $this->testProductData['mota_sp'],
            'gia_sp' => $this->testProductData['gia_sp'],
            'thuong_hieu' => $this->testProductData['thuong_hieu'],
            'loai_sp' => $this->testProductData['loai_sp'],
            'stock' => $this->testProductData['stock']
        ];

        $_FILES = [
            'filetoup' => [
                'name' => array_map(fn($file) => basename($file), $this->testProductData['filetoup']),
                'type' => ['image/jpeg', 'image/jpeg', 'image/jpeg', 'image/jpeg'],
                'tmp_name' => $this->testProductData['filetoup'],
                'error' => [0, 0, 0, 0],
                'size' => [512, 512, 512, 512]
            ]
        ];

        ob_start(); // Bắt đầu bộ đệm đầu ra
        include 'C:\Users\admin\Documents\Xamppnewinstall\htdocs\ProjectWeb\addProduct.html'; // Include file xử lý để kiểm tra
        $output = ob_get_clean(); // Lấy đầu ra

        // Kiểm tra dữ liệu được xử lý thành công
        $this->assertStringContainsString('Sản phẩm đã được thêm thành công', $output);
    }

    public function testMissingFields(): void
    {
        // Kiểm tra trường hợp thiếu tất cả các trường
        $_POST = [
            'ten_sp' => '', // Bỏ trống tên sản phẩm
            'ma_sp' => '', // Bỏ trống mã sản phẩm
            'mota_sp' => '', // Bỏ trống mô tả sản phẩm
            'gia_sp' => '', // Bỏ trống giá sản phẩm
            'thuong_hieu' => '0', // Không chọn thương hiệu
            'loai_sp' => '0', // Không chọn loại sản phẩm
            'stock' => '', // Không nhập số lượng
        ];

        $_FILES = [
            'filetoup' => [
                'name' => ['', '', '', ''], // Không tải lên file ảnh
                'type' => ['', '', '', ''],
                'tmp_name' => ['', '', '', ''],
                'error' => [4, 4, 4, 4], // Lỗi không tải file
                'size' => [0, 0, 0, 0]
            ]
        ];

        ob_start();
        include 'C:\Users\admin\Documents\Xamppnewinstall\htdocs\ProjectWeb\addProduct.html';
        $output = ob_get_clean();

        // Kiểm tra thông báo lỗi cho tất cả trường
        $this->assertStringContainsString('Bạn cần nhập tên, mã sản phẩm, mô tả chi tiết, giá bán, chọn thương hiệu, loại sản phẩm và tải đủ ảnh lên.', $output);
    }

    public function testMissingProductCode(): void
    {
        // Kiểm tra nếu thiếu mã sản phẩm
        $_POST = [
            'ten_sp' => $this->testProductData['ten_sp'],
            'ma_sp' => '', // Bỏ trống mã sản phẩm
            'mota_sp' => $this->testProductData['mota_sp'],
            'gia_sp' => $this->testProductData['gia_sp'],
            'thuong_hieu' => $this->testProductData['thuong_hieu'],
            'loai_sp' => $this->testProductData['loai_sp'],
            'stock' => $this->testProductData['stock']
        ];

        ob_start();
        include 'C:\Users\admin\Documents\Xamppnewinstall\htdocs\ProjectWeb\addProduct.html';
        $output = ob_get_clean();

        $this->assertStringContainsString('Bạn cần nhập mã sản phẩm.', $output);
    }

    public function testMissingDescription(): void
    {
        // Kiểm tra nếu thiếu mô tả sản phẩm
        $_POST = [
            'ten_sp' => $this->testProductData['ten_sp'],
            'ma_sp' => $this->testProductData['ma_sp'],
            'mota_sp' => '', // Bỏ trống mô tả sản phẩm
            'gia_sp' => $this->testProductData['gia_sp'],
            'thuong_hieu' => $this->testProductData['thuong_hieu'],
            'loai_sp' => $this->testProductData['loai_sp'],
            'stock' => $this->testProductData['stock']
        ];

        ob_start();
        include 'C:\Users\admin\Documents\Xamppnewinstall\htdocs\ProjectWeb\addProduct.html';
        $output = ob_get_clean();

        $this->assertStringContainsString('Bạn cần nhập mô tả chi tiết cho sản phẩm.', $output);
    }

    public function testInvalidBrandAndType(): void
    {
        // Kiểm tra nếu thương hiệu hoặc loại sản phẩm không được chọn
        $_POST = [
            'ten_sp' => $this->testProductData['ten_sp'],
            'ma_sp' => $this->testProductData['ma_sp'],
            'mota_sp' => $this->testProductData['mota_sp'],
            'gia_sp' => $this->testProductData['gia_sp'],
            'thuong_hieu' => '0', // Không chọn thương hiệu
            'loai_sp' => '0', // Không chọn loại sản phẩm
            'stock' => $this->testProductData['stock']
        ];

        ob_start();
        include 'C:\Users\admin\Documents\Xamppnewinstall\htdocs\ProjectWeb\addProduct.html';
        $output = ob_get_clean();

        $this->assertStringContainsString('Bạn cần chọn thương hiệu và loại sản phẩm.', $output);
    }

    public function testInvalidStockValue(): void
    {
        // Kiểm tra nếu số lượng không hợp lệ
        $_POST = [
            'ten_sp' => $this->testProductData['ten_sp'],
            'ma_sp' => $this->testProductData['ma_sp'],
            'mota_sp' => $this->testProductData['mota_sp'],
            'gia_sp' => $this->testProductData['gia_sp'],
            'thuong_hieu' => $this->testProductData['thuong_hieu'],
            'loai_sp' => $this->testProductData['loai_sp'],
            'stock' => 10 // Giá trị dưới 20
        ];

        $_FILES = [
            'filetoup' => [
                'name' => array_map(fn($file) => basename($file), $this->testProductData['filetoup']),
                'type' => ['image/jpeg', 'image/jpeg', 'image/jpeg', 'image/jpeg'],
                'tmp_name' => $this->testProductData['filetoup'],
                'error' => [0, 0, 0, 0],
                'size' => [512, 512, 512, 512]
            ]
        ];

        ob_start();
        include 'C:\Users\admin\Documents\Xamppnewinstall\htdocs\ProjectWeb\addProduct.html';
        $output = ob_get_clean();

        // Kiểm tra thông báo lỗi khi stock không hợp lệ
        $this->assertStringContainsString('Số lượng nhập kho phải tối thiểu là 20.', $output);
    }
}
?>
