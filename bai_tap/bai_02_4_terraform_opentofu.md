# Terraform MPL → BUSL và sự ra đời của OpenTofu

## 1. Bối cảnh

Terraform là một công cụ Infrastructure as Code (IaC) do HashiCorp phát triển, cho phép người dùng mô tả và quản lý hạ tầng như máy chủ, mạng, cơ sở dữ liệu và các dịch vụ cloud bằng mã cấu hình. Terraform được phát hành dưới giấy phép Mozilla Public License 2.0 (MPL 2.0) từ năm 2014. Trong nhiều năm, Terraform trở thành một dự án quan trọng trong hệ sinh thái DevOps và cloud, đồng thời tạo ra một cộng đồng lớn gồm người dùng, nhà phát triển và nhiều dự án, module, provider liên quan.

Tuy nhiên, ngày 10/08/2023, HashiCorp công bố thay đổi giấy phép đối với các sản phẩm cốt lõi của mình. Các phiên bản Terraform phát hành trong tương lai chuyển từ MPL 2.0 sang Business Source License 1.1 (BUSL). HashiCorp cho biết mục tiêu của thay đổi này là bảo vệ hoạt động kinh doanh trước các công ty có thể sử dụng sản phẩm của HashiCorp để xây dựng dịch vụ cạnh tranh trực tiếp.

Điểm quan trọng là việc thay đổi này áp dụng cho các phiên bản phát hành trong tương lai, không có nghĩa toàn bộ mã nguồn Terraform trong lịch sử bỗng trở thành BUSL. Đây chính là cơ sở để cộng đồng có thể fork phiên bản Terraform cuối cùng còn được cấp phép theo MPL 2.0.

## 2. Từ MPL 2.0 sang BUSL

MPL 2.0 là một giấy phép mã nguồn mở được Mozilla phát triển. Nó cho phép sử dụng, sửa đổi và phân phối phần mềm theo các điều kiện của giấy phép. MPL có tính chất "file-level copyleft", nghĩa là khi phân phối các file đã được sửa đổi thuộc MPL, các yêu cầu của MPL có thể áp dụng đối với những file đó, trong khi vẫn cho phép kết hợp với mã nguồn có giấy phép khác trong nhiều trường hợp.

BUSL có cách tiếp cận khác. Đây không phải là một giấy phép mã nguồn mở theo cách MPL 2.0 được công nhận. HashiCorp vẫn cho phép sử dụng phần mềm trong nhiều trường hợp, nhưng đặt ra các giới hạn liên quan đến việc cung cấp dịch vụ hoặc sản phẩm cạnh tranh với sản phẩm của HashiCorp.

Theo HashiCorp, BUSL không cấm nhà phát triển tạo ra các sản phẩm cạnh tranh nói chung, nhưng hạn chế một số hình thức cung cấp dịch vụ hoặc sử dụng sản phẩm HashiCorp nhằm cạnh tranh trực tiếp với chính sản phẩm đó.

Điều này tạo ra một vấn đề lớn đối với cộng đồng. Với một dự án hạ tầng được sử dụng rộng rãi, người dùng và doanh nghiệp cần biết rõ họ có thể sử dụng phần mềm như thế nào trong sản phẩm hoặc dịch vụ thương mại. Sự thay đổi giấy phép làm xuất hiện những câu hỏi về phạm vi sử dụng, khả năng xây dựng sản phẩm dựa trên Terraform và mức độ phụ thuộc vào quyết định của một công ty duy nhất.

## 3. Sự ra đời của OpenTofu

Trước thay đổi của HashiCorp, một nhóm các công ty và thành viên cộng đồng đã đưa ra OpenTofu, ban đầu được gọi là OpenTF. Mục tiêu là duy trì một phiên bản Terraform thực sự mã nguồn mở và được quản trị theo hướng trung lập.

Ngày 25/08/2023, nhóm OpenTofu chính thức công bố đã fork Terraform sau khi HashiCorp không đảo ngược quyết định thay đổi giấy phép. Nhóm cho biết OpenTofu sẽ hướng tới các đặc điểm quan trọng: thực sự mã nguồn mở, do cộng đồng định hướng, trung lập với nhà cung cấp và tương thích với hệ sinh thái Terraform.

Ngày 05/09/2023, repository OpenTofu được công khai. Dự án được fork từ phiên bản Terraform cuối cùng còn sử dụng MPL 2.0. Điều này cho phép cộng đồng tiếp tục phát triển dự án dựa trên phần mã nguồn có giấy phép phù hợp. OpenTofu cũng đặt mục tiêu trở thành một lựa chọn thay thế có khả năng tương thích cao với Terraform.

Đến ngày 20/09/2023, Linux Foundation công bố OpenTofu như một dự án mã nguồn mở thay thế Terraform. Việc đưa dự án vào Linux Foundation có ý nghĩa quan trọng vì giúp OpenTofu có cơ chế quản trị trung lập hơn, thay vì phụ thuộc vào một công ty duy nhất.

## 4. Ý nghĩa đối với người dùng và doanh nghiệp

Sự kiện Terraform chuyển từ MPL 2.0 sang BUSL cho thấy giấy phép phần mềm có thể ảnh hưởng trực tiếp đến chiến lược công nghệ của doanh nghiệp. Khi một doanh nghiệp sử dụng một công cụ mã nguồn mở lâu dài, họ không chỉ quan tâm đến tính năng mà còn phải quan tâm đến giấy phép, quyền sử dụng và nguy cơ thay đổi giấy phép trong tương lai.

OpenTofu tạo ra một lựa chọn khác cho các doanh nghiệp muốn tiếp tục sử dụng hệ sinh thái Terraform nhưng ưu tiên giấy phép mã nguồn mở. OpenTofu cung cấp khả năng tương thích với các phiên bản Terraform trước đây và có hướng dẫn chính thức để chuyển đổi từ Terraform sang OpenTofu.

Tuy nhiên, chuyển sang OpenTofu cũng không hoàn toàn không có rủi ro. Doanh nghiệp phải kiểm tra khả năng tương thích của module, provider, CI/CD pipeline và các công cụ liên quan. Ngoài ra, việc duy trì hai hệ sinh thái Terraform và OpenTofu có thể khiến cộng đồng bị phân tách, từ đó làm tăng chi phí kiểm thử và bảo trì.

## 5. Bài học về quản lý giấy phép phần mềm

Theo em, trường hợp Terraform và OpenTofu là một ví dụ rõ ràng cho thấy doanh nghiệp không nên xem giấy phép mã nguồn mở chỉ là một vấn đề pháp lý phụ trợ. License có thể quyết định khả năng sử dụng, sửa đổi, phân phối và xây dựng sản phẩm thương mại dựa trên một phần mềm.

Đối với doanh nghiệp, trước khi lựa chọn một công nghệ mã nguồn mở quan trọng, cần kiểm tra ít nhất ba vấn đề: giấy phép hiện tại, lịch sử thay đổi giấy phép và chính sách quản trị của dự án. Đồng thời, cần lập danh sách các dependency và theo dõi license của chúng trong suốt vòng đời sản phẩm.

Trường hợp Terraform cũng cho thấy giá trị của việc có một cộng đồng và cơ chế quản trị trung lập. Khi OpenTofu được Linux Foundation hỗ trợ, người dùng có thêm một lựa chọn nhằm giảm sự phụ thuộc vào một nhà cung cấp duy nhất.

Tóm lại, việc HashiCorp chuyển Terraform từ MPL 2.0 sang BUSL năm 2023 đã tạo ra một bước ngoặt lớn trong hệ sinh thái Infrastructure as Code. Sự ra đời của OpenTofu cho thấy giấy phép phần mềm không chỉ ảnh hưởng đến quyền pháp lý mà còn có thể dẫn đến việc hình thành một dự án mã nguồn mở mới. Đây là bài học quan trọng đối với cả lập trình viên và doanh nghiệp khi lựa chọn và sử dụng phần mềm mã nguồn mở.

## Tài liệu tham khảo

1. HashiCorp, "HashiCorp projects changing license to Business Source License v1.1", 2023.
2. HashiCorp, "HashiCorp updates licensing FAQ based on community questions", 2023.
3. OpenTofu, "OpenTofu Announces Fork of Terraform", 2023.
4. OpenTofu, "The OpenTofu fork is now available!", 2023.
5. Linux Foundation, "Linux Foundation Launches OpenTofu: A New Open Source Alternative to Terraform", 2023.
