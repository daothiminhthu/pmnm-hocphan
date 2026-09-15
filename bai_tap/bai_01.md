# Elasticsearch và OpenSearch: khi giấy phép trở thành ranh giới cạnh tranh

**Đào Thị Minh Thư — 23T1020523 — CNTT K47B**

## Bối cảnh dự án gốc

Elasticsearch là công cụ tìm kiếm và phân tích dữ liệu mã nguồn mở, ra đời năm 2010, được công ty Elastic NV phát triển và phát hành theo giấy phép Apache 2.0 — một giấy phép cho phép sử dụng, sửa đổi và phân phối lại tự do, kể cả cho mục đích thương mại. Nhờ tính linh hoạt đó, Elasticsearch nhanh chóng trở thành hạ tầng phổ biến cho việc tìm kiếm log, giám sát hệ thống và phân tích dữ liệu lớn, được nhiều nhà cung cấp dịch vụ đám mây, trong đó có Amazon Web Services (AWS), đóng gói thành dịch vụ quản lý sẵn để bán lại cho khách hàng.

## Nguyên nhân dẫn đến mâu thuẫn

Vấn đề nảy sinh khi Elastic nhận thấy các nhà cung cấp đám mây lớn, đặc biệt là AWS, vận hành dịch vụ Elasticsearch có thu phí trên nền tảng của họ mà không đóng góp trở lại cho việc phát triển dự án gốc, cũng không chia sẻ doanh thu với Elastic. Đây chính là mô hình mà bài giảng gọi là hiện tượng doanh nghiệp lớn "khai thác miễn phí" hạ tầng mã nguồn mở do người khác gây dựng.

Để ngăn tình trạng này, ngày 21 tháng 1 năm 2021, Elastic công bố sẽ đổi giấy phép của Elasticsearch và Kibana kể từ phiên bản 7.11, chuyển từ Apache 2.0 sang mô hình cấp phép kép: Server Side Public License (SSPL) hoặc Elastic License. SSPL là giấy phép copyleft mạnh, yêu cầu bất kỳ ai cung cấp phần mềm dưới dạng dịch vụ phải công bố toàn bộ mã nguồn của hệ thống vận hành dịch vụ đó theo cùng giấy phép — điều khoản này khiến SSPL không được OSI công nhận là mã nguồn mở, vì vi phạm tiêu chí không phân biệt lĩnh vực sử dụng.

## Quá trình tách nhánh

AWS phản ứng gần như ngay lập tức. Chỉ vài ngày sau thông báo của Elastic, AWS tuyên bố sẽ duy trì một nhánh Apache 2.0, và đến ngày 12 tháng 4 năm 2021 chính thức công bố dự án OpenSearch — bản fork từ phiên bản cuối cùng còn giữ giấy phép Apache 2.0 là Elasticsearch 7.10.2 và Kibana 7.10.2. OpenSearch 1.0 được phát hành ngày 12 tháng 7 năm 2021, và dịch vụ Amazon Elasticsearch Service được đổi tên thành Amazon OpenSearch Service vào tháng 9 cùng năm.

Điểm đáng chú ý là quyết định của AWS không đơn thuần vì lý do kỹ thuật, mà là hệ quả trực tiếp của quyền tự do số 3 trong bốn quyền tự do phần mềm: một khi mã nguồn đã từng được phát hành theo giấy phép mở, quyền đó không thể bị thu hồi đối với các phiên bản đã công bố, nên cộng đồng hoàn toàn có thể lấy phiên bản cuối cùng còn mở để phát triển tiếp độc lập.

## Tình trạng hiện nay của hai nhánh

Sau gần năm năm, hai dự án đã phân hóa rõ rệt. Elasticsearch tiếp tục thuộc quyền kiểm soát của Elastic, duy trì cấp phép SSPL và Elastic License, đến năm 2024 bổ sung thêm lựa chọn AGPLv3 — một giấy phép được OSI công nhận — nhằm xoa dịu chỉ trích về việc "đóng" sản phẩm. Tuy nhiên các bản phân phối mặc định và dịch vụ thương mại của Elastic vẫn giữ Elastic License, và nhiều tính năng nâng cao vẫn nằm sau gói trả phí.

Về phía OpenSearch, dự án giữ nguyên giấy phép Apache 2.0 và đến tháng 9 năm 2024 được AWS chuyển giao quyền quản trị cho Linux Foundation dưới tên OpenSearch Software Foundation, với sự tham gia điều hành của nhiều tổ chức như SAP và Uber, không còn phụ thuộc riêng vào một doanh nghiệp. Đến năm 2026, OpenSearch đã thu hút hơn 400 tổ chức và khoảng 3.300 người đóng góp.

## Bài học rút ra

Trường hợp Elasticsearch và OpenSearch cho thấy quyền tự do phân phối lại bản đã sửa đổi không chỉ là nguyên tắc pháp lý trừu tượng, mà là công cụ thực tế giúp cộng đồng "cứu" một dự án khi doanh nghiệp chủ quản thay đổi định hướng. Đồng thời, câu chuyện cũng minh họa cho căng thẳng cố hữu giữa mô hình kinh doanh mã nguồn mở và lợi ích của các nhà cung cấp hạ tầng đám mây quy mô lớn — vấn đề mà nhiều dự án khác như MongoDB, Terraform hay Redis cũng gặp phải trong giai đoạn 2018–2024.
