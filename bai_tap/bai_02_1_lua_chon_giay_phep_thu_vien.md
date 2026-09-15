# Lựa chọn giấy phép cho thư viện Python xử lý tiếng Việt

## Bối cảnh
Thư viện xử lý tiếng Việt (tách từ, chuẩn hóa dấu, nhận dạng thực thể...) là loại công cụ nền tảng mà càng nhiều dự án khác dùng được thì càng có giá trị — kể cả trong sản phẩm thương mại đóng nguồn của công ty khác, ứng dụng di động, hay dịch vụ SaaS. Mục tiêu ưu tiên là tối đa hóa lượt sử dụng và lượt đóng góp, không phải kiểm soát cách người khác dùng lại mã nguồn.

## Giấy phép được chọn: MIT

**Lý do chọn nhóm dễ dãi (permissive) thay vì copyleft**

Nếu chọn GPL hoặc AGPL, bất kỳ công ty nào muốn tích hợp thư viện vào sản phẩm đóng nguồn của họ sẽ bị buộc phải công bố toàn bộ mã nguồn sản phẩm đó. Điều này sẽ khiến bộ phận pháp chế của họ loại thư viện ngay từ khâu rà soát — đúng như tình huống thực tế bài giảng đã nêu: "dự án không có giấy phép phù hợp sẽ không được doanh nghiệp nào sử dụng". Với một thư viện tiện ích nền tảng, rào cản này triệt tiêu chính mục tiêu phổ biến rộng rãi.

**Lý do chọn MIT thay vì Apache-2.0**

Cả hai đều thuộc nhóm dễ dãi và đều cho phép dùng thương mại tự do. Khác biệt nằm ở điều khoản cấp phép sáng chế của Apache-2.0. Một thư viện xử lý ngôn ngữ tự nhiên thường dùng thuật toán, không phải phát minh có khả năng bị tranh chấp sáng chế cao như phần cứng hay mã hóa. Vì rủi ro sáng chế thấp, phần bổ sung của Apache-2.0 (điều khoản trả đũa sáng chế, yêu cầu giữ tệp NOTICE) tạo thêm gánh nặng tuân thủ cho người dùng thư viện mà không mang lại lợi ích tương xứng. MIT, với văn bản chỉ khoảng 170 từ, dễ đọc, dễ hiểu, đã là chuẩn mực trong hệ sinh thái Python (nhiều gói phổ biến dùng BSD/MIT).

## Kết luận
MIT là lựa chọn phù hợp nhất: cho phép sử dụng, sửa đổi, phân phối lại — kể cả trong sản phẩm đóng nguồn — chỉ với điều kiện giữ thông báo bản quyền. Điều này tối đa hóa khả năng thư viện được các dự án khác, kể cả doanh nghiệp, đưa vào sử dụng, đồng thời giữ thủ tục tuân thủ tối giản cho người dùng cuối.
