# Kết quả rà soát giấy phép phụ thuộc

## Lệnh sử dụng

```bash
pip install flask requests pandas pip-licenses
pip-licenses --format=markdown --with-urls
```

## Bảng kết quả

| Name | Version | License | URL |
|---|---|---|---|
| charset-normalizer | 3.5.1 | MIT | https://github.com/jawah/charset_normalizer/blob/master/CHANGELOG.md |
| click | 8.5.0 | BSD-3-Clause | https://github.com/pallets/click/ |
| idna | 3.19 | BSD-3-Clause | https://github.com/kjd/idna |
| itsdangerous | 2.2.0 | BSD License | https://github.com/pallets/itsdangerous/ |
| numpy | 2.5.3 | BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0 | https://numpy.org |
| pandas | 3.0.5 | BSD License | https://pandas.pydata.org |
| python-dateutil | 2.9.0.post0 | Apache Software License; BSD License | https://github.com/dateutil/dateutil |
| requests | 2.34.2 | Apache Software License | https://github.com/psf/requests |
| six | 1.17.0 | MIT License | https://github.com/benjaminp/six |
| tzdata | 2026.4 | Apache-2.0 | https://github.com/python/tzdata |
| urllib3 | 2.7.0 | MIT | https://github.com/urllib3/urllib3/blob/main/CHANGES.rst |

## Phân tích

- Tổng số gói: **11**
- Gói thuộc nhóm copyleft mạnh (GPL/AGPL): **Không có**
- Các giấy phép xuất hiện chủ yếu là MIT, BSD và Apache-2.0.
- Đây đều là các giấy phép tương đối dễ dãi, cho phép sử dụng các thư viện trong phần mềm thương mại đóng nguồn nếu tuân thủ các điều kiện của giấy phép.

## Kết luận

Nếu dự án là phần mềm thương mại đóng nguồn, các gói trong danh sách có thể được sử dụng mà không phát sinh nghĩa vụ phải công khai mã nguồn của toàn bộ dự án.

Tuy nhiên, vẫn phải tuân thủ các điều kiện của từng giấy phép, đặc biệt là giữ lại thông báo bản quyền và bản sao giấy phép của các thành phần được sử dụng khi phân phối phần mềm.

Đối với các thành phần sử dụng Apache-2.0 hoặc Apache Software License, cần kiểm tra và giữ lại tệp NOTICE nếu thư viện có cung cấp NOTICE.

Qua kết quả rà soát 11 gói, không phát hiện giấy phép GPL hoặc AGPL nên dự án không phát sinh nghĩa vụ copyleft mạnh từ các phụ thuộc này.