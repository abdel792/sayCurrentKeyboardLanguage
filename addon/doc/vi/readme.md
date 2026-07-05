# sayCurrentKeyboardLanguage

* Tác giả: Abdel, Noelia.

# Giới thiệu #

Tiện ích mở rộng này được tạo ra theo yêu cầu của một thành viên trên danh sách thư điện tử nvda-addons.

Nó cung cấp một lệnh kịch bản (script) không được gán phím tắt mặc định, cho phép lấy và đọc ngôn ngữ bàn phím hiện tại.

Nếu nhấn hai lần, nó sẽ đọc ngôn ngữ mặc định của hệ thống.

Trong phiên bản đầu tiên của mô-đun này, nó được đề xuất như một globalPlugin đơn giản để dán vào thư mục cấu hình của NVDA, sau đó đã được chuyển đổi thành một tiện ích mở rộng (addon).

## Lưu ý ##

Để gán phím tắt cho lệnh kịch bản đọc ngôn ngữ bàn phím, hãy làm theo các bước sau:

* Mở menu NVDA bằng tổ hợp phím "NVDA + N";
* Đi tới menu Cấu hình (Preferences) của NVDA;
* Sau đó đi tới menu con "Phím tắt lệnh" (Input gestures).
* Tiếp theo, chọn danh mục "Nhập liệu" (Input) và mở nó bằng phím mũi tên phải.
* Di chuyển đến mục có nhãn "Đọc ngôn ngữ bàn phím đang sử dụng, nếu nhấn hai lần, đọc ngôn ngữ mặc định của hệ thống";
* Sau khi hoàn tất, nhấn Alt + A để thêm phím tắt, và nhập "NVDA + F4" hoặc một phím tắt khác tùy bạn chọn;
* Tiếp theo, nhấn phím mũi tên lên một lần, bạn sẽ nghe thấy "phím tắt bạn đã chọn, tất cả các bố cục";
* Xác nhận bằng phím Enter, sau đó dùng Tab để di chuyển đến nút OK và nhấn Enter;
* Phím tắt đã chọn sau đó sẽ kích hoạt lệnh kịch bản đọc ngôn ngữ bàn phím.

## Tính tương thích ##

* Tiện ích này tương thích với các phiên bản NVDA từ 2019.3 trở về sau.

## Thay đổi cho phiên bản 20240326.0.0

* Cập nhật tính tương thích cho nvda-2024.1;
* Xóa liên kết tải xuống khỏi tệp readme, liên kết tải xuống cho các bản cập nhật tương lai giờ đây sẽ chỉ có sẵn từ cửa hàng tiện ích (Add-on Store).

## Thay đổi cho phiên bản 20231229.0.0 ##

* Thêm một triển khai tương thích ngược để hỗ trợ chế độ giọng nói theo yêu cầu (speech on demand), chế độ này sẽ sớm có sẵn trên nvda-2024.1.

## Thay đổi cho phiên bản 20230729.0.0 ##

* Áp dụng các quy tắc của flake8 và mypy cho mã nguồn;
* Thay đổi phiên bản NVDA tối thiểu được hỗ trợ thành 2019.3 để hỗ trợ các kiểu dữ liệu (annotations) được giới thiệu trong Python 3.
* Loại bỏ phím tắt "NVDA + F4" dùng để gọi lệnh kịch bản đọc ngôn ngữ bàn phím, nhằm cho phép người dùng tự chọn phím tắt ưa thích của họ.

## Thay đổi cho phiên bản 20230607.0.0 ##

* Thêm các quy trình làm việc (workflows) sau:
 * auto-update-translations - để tự động cập nhật bản dịch từ hệ thống dịch thuật của NVDA.
 * release-on-tag..yaml: để biên dịch và phát hành tiện ích ngay khi có một thẻ (tag) mới được đẩy lên;
 * manual-release.yaml: để biên dịch và phát hành các phiên bản mới của tiện ích một cách thủ công.
* Cập nhật các bản dịch.

## Thay đổi cho phiên bản 20230426.0.0 và các phiên bản sau ##

* • Thay đổi số phiên bản, phiên bản NVDA tối thiểu và liên kết tải xuống theo các quy ước/yêu cầu của cửa hàng tiện ích.

## Thay đổi cho phiên bản 19.02 ##

* Thay đổi cách đánh số phiên bản bằng cách sử dụng định dạng YY.MM (Năm gồm 2 chữ số, theo sau là dấu chấm, và tháng gồm 2 chữ số);
* Thêm tính tương thích với định dạng đánh số phiên bản mới của tiện ích mở rộng, xuất hiện từ bản nvda 2019.1.

## Thay đổi cho phiên bản 1.1 ##

* Tiện ích được đổi tên từ getCurKeyboardLanguage thành sayCurrentKeyboardLanguage;
* Thêm giấy phép GPL vào tiện ích;
* Thêm lệnh kịch bản getCurKeyboardLanguage vào danh mục "Trạng thái hệ thống";
* Sửa một số lỗi trong mã nguồn.

## Thay đổi cho phiên bản 1.0 ##

* Phiên bản đầu tiên.
