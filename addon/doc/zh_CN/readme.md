# sayCurrentKeyboardLanguage-NVDA语言显示插件 #

* 作者: Abdel, Noelia;
* Download [stable
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Download [development
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# 介绍 #

此加载项是根据 nvda-addons 邮件列表中的成员的请求创建的。

它提供了一个键盘快捷方式, NVDA + F4, 它允许检索和提供当前键盘的语言。

如果按两次, 则提供系统的默认语言。

在这个模块的第一个版本中，它被建议作为简单的globalPlugin粘贴到NVDA的配置目录中，然后将其转换为插件。

## 注意 ##

如果NVDA +
F4键盘快捷键与另一个快捷键冲突，您可以通过转到NVDA的“设置”菜单，在“输入手势”子菜单中进行更改。然后，您将在“系统状态”类别中找到该脚本。

快捷键可以在“系统状态”类别找到。

## 兼容性 ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  and beyond.

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
