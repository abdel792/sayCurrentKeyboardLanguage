# sayCurrentKeyboardLanguage (Повідомити поточну мову клавіатури) #

* Автори: Abdel, Noelia;
* Download [stable
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Download [development
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Презентація #

Цей додаток було створено на прохання учасника поштової конференції додатків
для NVDA.

It provides a script without gesture, which allows to retrieve and give the
language of the current keyboard.

Якщо натиснути двічі, повідомляє основну мову системи.

Перша версія цього модуля була простим плагіном, який треба було вставити
вручну до папки з конфігурацією NVDA. Однак тепер його перетворено у
додаток.

## Примітки ##

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

## Сумісність ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230729.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.
* Removed the "NVDA + F4" gesture calling the script giving the keyboard
  language., to allow users to choose their preferred gesture.

## Зміни у версії 20230426.0.0

* Змінено номер версії, мінімальну версію NVDA та посилання для завантаження
  відповідно до правил/вимог магазину.

## Зміни у версії 19.02 ##

* Змінено нумерацію версій за допомогою РР.ММ (рік - 2 цифри, потім крапка,
  потім місяць - 2 цифри);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Зміни з версії 1.1 ##

* Додаток перейменовано з getCurKeyboardLanguage на
  sayCurrentKeyboardLanguage;
* До додатка додано ліцензію GPL;
* Сценарій getCurKeyboardLanguage додано в категорію "Статус системи";
* Виправлено деякі помилки у коді.

## Зміни з версії 1.0 ##

* Перша версія.

[[!tag dev stable]]
