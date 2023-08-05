# Báo ngôn ngữ bàn phím hiện tại #

* Tác giả: Abdel, Noelia;
* Download [stable
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Download [development
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Trình bày #

Addon được tạo ra theo đề nghị từ một thành viên trên diễn đàn trao đổi qua
thư điện tử của  nvda-addons.

It provides a script without gesture, which allows to retrieve and give the
language of the current keyboard.

Nếu bấm hai lần, cho biết ngôn ngữ mặc định của hệ thống.

Ở phiên bản đầu tiên của module này, nó được đề nghị như là một globalPlugin
đơn giản để dán vào thư mục cấu hình của NVDA, rồi nó đã được chuyển thành
một addon.

## Lưu ý ##

To set a gesture to the script giving the keyboard language, follow these
steps:

* Open the NVDA's menu, with "NVDA + N";
* Go to NVDA's preferences menu;
* Then go to the submenu "Input gestures".
* Then select the category "Input", and open it with right arrow.
* Go to the item labeled "Gives the language of the keyboard in use, if
  pressed twice, give the default language of the system";
* Once done, press Alt + A to add a gesture, and type "NVDA + F4" or another
  gesture of your choice;
* This done, press the up arrow once, you hear "your chosen gesture, all
  layout";
* Validate on enter, then tab to OK then enter;
* Your chosen gesture should then call the script giving keyboard language.

## Tương thích ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230729.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.
* Removed the "NVDA + F4" gesture calling the script giving the keyboard
  language., to allow users to choose their preferred gesture.

## Changes for version 20230426.0.0 and beyond##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Các thay đổi cho phiên bản 19.02 ##

* Thay đổi cách đặt số phiên bản bằng YY.MM (hai chữ số năm, một dấu chấm,
  hai chữ số tháng);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Các thay đổi cho phiên bản 1.1 ##

* Added đã được đổi tên từ getCurKeyboardLanguage thành
  sayCurrentKeyboardLanguage;
* Thêm giấy phép GPL vào addon;
* Thêm kịch bản getCurKeyboardLanguage vào phần "Trạng thái hệ thống";
* Sửa vài lỗi trong mã nguồn.

## Các thay đổi cho phiên bản 1.0 ##

* Phiên bản đầu tiên.

[[!tag dev stable]]
