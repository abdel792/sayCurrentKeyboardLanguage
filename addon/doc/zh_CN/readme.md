# sayCurrentKeyboardLanguage-NVDA语言显示插件 #

* 作者: Abdel, Noelia;
* Download [stable
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Download [development
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# 介绍 #

此加载项是根据 nvda-addons 邮件列表中的成员的请求创建的。

It provides a script without gesture, which allows to retrieve and give the
language of the current keyboard.

如果按两次, 则提供系统的默认语言。

在这个模块的第一个版本中，它被建议作为简单的globalPlugin粘贴到NVDA的配置目录中，然后将其转换为插件。

## 注意 ##

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

## 兼容性 ##

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

## 19.02版的更改 ##

* 现在使用YY.MM形式的版本号（年份为2位数，后跟一个点，后跟月份为2位数）;
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## 版本1.1 ##

* 插件已从getCurKeyboardLanguage重命名为sayCurrentKeyboardLanguage;
* 在插件中添加了GPL许可证;
* 将脚本getCurKeyboardLanguage添加到“系统状态”类别;
* 修复了代码中的一些错误。

## 版本1.0 ##

* 发布初始版本。

[[!tag dev stable]]
