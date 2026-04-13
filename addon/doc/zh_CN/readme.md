# 读出当前键盘语言

* 作者：Abdel, Noelia；
* 下载 [稳定版][1]
* 下载 [开发版][2]

# 功能概述 #

此插件由 nvda-addons 邮件列表成员的请求而开发。

提供了一个未分配快捷键的命令，可用于获取并读出当前键盘语言。

连按两次将读出系统默认语言。

该模块的初始版本曾建议以全局插件形式直接粘贴至 NVDA 配置目录使用，现已正式转换为插件形式发布。

## 使用说明 ##

为读出键盘语言命令设置快捷键的操作步骤：

* 按 NVDA+N 打开 NVDA 菜单；
* 进入"选项"菜单；
* 选择"输入手势"菜单。
* 选择“输入”类别后按右光标键展开。
* 定位至"给出正在使用的键盘的语言。如果按两次，则给出系统的默认语言"项；
* 按 Alt+A 添加快捷键，按下 NVDA+F4 或其他快捷键；
* 按上光标键将输入的快捷键设为全局生效；
* 按回车确认，Tab 键跳至"确定"按钮后再次回车；
* 此后使用自定义手势即可触发键盘语言播报功能。

## 兼容性 ##

* 此插件兼容 NVDA 2019.3 及更高版本。

## 20230729.0.0 版本变更 ##

* 对代码应用 flake8 和 mypy 规范；
* 最低支持版本调整为 NVDA 2019.3 以支持 Python 3 类型注解。
* 移除原 NVDA+F4 默认快捷键，允许用户自定义。

## 20230607.0.0 版本变更 ##

* 新增以下工作流：
 * auto-update-translations：自动从 NVDA 翻译系统更新翻译。
 * release-on-tag.yaml：推送新标签时自动构建发布插件；
 * manual-release.yaml：手动构建发布新版本插件。
* 更新翻译。

## 20230426.0.0 及后续版本变更 ##

* 根据商店规范调整版本号、NVDA 版本最低要求及下载链接。

## 19.02 版本变更 ##

* 采用 YY.MM 格式版本编号（2位年份+小数点+2位月份）；
* 适配 NVDA 2019.1 启用的新插件版本格式。

## 1.1 版本变更 ##

* 插件名称由 getCurKeyboardLanguage 更改为 sayCurrentKeyboardLanguage；
* 添加 GPL 许可证；
* 将脚本归类至"系统状态"类别；
* 修复代码中的若干错误。

## 1.0 版本变更 ##

* 初始版本。

[1]: https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage

[2]: https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage
