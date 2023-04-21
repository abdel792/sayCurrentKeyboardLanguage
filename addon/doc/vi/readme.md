# Báo ngôn ngữ bàn phím hiện tại #

* Tác giả: Abdel, Noelia;
* Tải về [phiên bản chính thức][1];
* Tải về [bản thử nghiệm][2].

# Trình bày #

Addon được tạo ra theo đề nghị từ một thành viên trên diễn đàn trao đổi qua
thư điện tử của  nvda-addons.

Nó cung cấp phím lệnh NVDA + F4 để xác định và cho biết ngôn ngữ hiện tại
của bàn phím.  Nếu bấm hai lần sẽ cho biết ngôn ngữ mặc định của hệ thống.

Nếu bấm hai lần, cho biết ngôn ngữ mặc định của hệ thống.

Ở phiên bản đầu tiên của module này, nó được đề nghị như là một globalPlugin
đơn giản để dán vào thư mục cấu hình của NVDA, rồi nó đã được chuyển thành
một addon.

## Lưu ý ##

Nếu phím lệnh NVDA + F4 bị xung đột với một lệnh khác, bạn có thể thay đổi
bằng cách vào trình đơn cấu hình của NVDA, trong phần "Quản lý thao tác".

Rồi bạn sẽ tìm thấy kịch bản trong phân loại "Trạng thái hệ thống".

## Tương thích ##

* Add-on này tương thích với các phiên bản NVDA từ 2014.3 đến 2019.3.

## Các thay đổi cho phiên bản 19.02 ##

* Thay đổi cách đặt số phiên bản bằng YY.MM (hai chữ số năm, một dấu chấm,
  hai chữ số tháng);
* Thêm tương thích với định dạng phiên bản mới của add-on, xuất hiện từ nvda
  2019.1.

## Các thay đổi cho phiên bản 1.1 ##

* Added đã được đổi tên từ getCurKeyboardLanguage thành
  sayCurrentKeyboardLanguage;
* Thêm giấy phép GPL vào addon;
* Thêm kịch bản getCurKeyboardLanguage vào phần "Trạng thái hệ thống";
* Sửa vài lỗi trong mã nguồn.

## Các thay đổi cho phiên bản 1.0 ##

* Phiên bản đầu tiên.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=ckbl

[2]: https://www.nvaccess.org/addonStore/legacy?file=ckbl-dev
