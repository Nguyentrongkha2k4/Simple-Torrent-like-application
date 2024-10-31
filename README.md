# Simple-Torrent-like-application

## Hướng dẫn sử dụng

### Bước 1: Tải mã nguồn

- git clone [https://github.com/Nguyentrongkha2k4/Simple-Torrent-like-application.git](https://github.com/Nguyentrongkha2k4/Simple-Torrent-like-application.git)

### Bước 2: Khởi chạy file server trong mạng cục bộ

- python server.py

### Bước 3: Cài đặt:

- Đầu tiên bạn cần cấu hình lại file client bằng cách tìm kiếm câu lệnh sau:
`def __init__(self, serverhost='192.168.31.170', serverport=30000, server_info=('192.168.31.170', 40000))`
- Sau đó thay địa chỉ của server_info là "192.168.31.170" bằng địa chỉ mạng cục bộ của máy đang chạy server ở bước 2.
### Bước 4: Khởi động file client và thực hiện quá trình chuyển file như trong tài liệu hướng dẫn:
- python client.py