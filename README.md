# Dự án Mã hóa Python

Dự án này triển khai các thuật toán mã hóa và giải mã AES và DES bằng Python. Cấu trúc của dự án được thiết kế rõ ràng với sự phân tách rõ ràng các module cho mỗi thuật toán và các hàm tiện ích cho việc xử lý tệp tin.

## Cấu trúc Dự án



```
AES_DES_midterm_KTD
├── src
│   ├── aes
│   │   ├── __init__.py
│   │   ├── aes_encrypt.py
│   │   ├── aes_decrypt.py
│   │   └── aes_utils.py
│   ├── des
│   │   ├── __init__.py
│   │   ├── des_encrypt.py
│   │   ├── des_decrypt.py
│   │   └── des_utils.py
│   └── utils
│       ├── __init__.py
│       └── file_handler.py
├── data
│   ├── input.txt
│   ├── output_aes.txt
│   └── output_des.txt
├── main.py
└── README.md
```


## Tính năng

- **Mã hóa và Giải mã AES**: Được triển khai trong module `src/aes`.
- **Mã hóa và Giải mã DES**: Được triển khai trong module `src/des`.
- **Xử lý tệp tin**: Các hàm tiện ích để đọc dữ liệu đầu vào và ghi kết quả được đặt trong `src/utils/file_handler.py`.

## Cách sử dụng

1. Đặt văn bản gốc của bạn vào tệp `data/input.txt`.
2. Chạy script `main.py` để thực hiện mã hóa và giải mã.
3. Kết quả mã hóa sẽ được lưu vào tệp `data/output_aes.txt` cho AES và `data/output_des.txt` cho DES.

## Yêu cầu

- Python 3.x

## Cách chạy

Để thực thi dự án, bạn chỉ cần di chuyển đến thư mục dự án và chạy lệnh:
 `python main.py`
Lệnh này sẽ đọc dữ liệu từ tệp `data/input.txt`, thực hiện mã hóa bằng cả hai thuật toán AES và DES, và ghi kết quả vào các tệp đầu ra tương ứng.
