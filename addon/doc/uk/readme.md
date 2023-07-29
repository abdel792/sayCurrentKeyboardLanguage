# sayCurrentKeyboardLanguage (Повідомити поточну мову клавіатури) #

* Автори: Abdel, Noelia;
* Download [stable
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Download [development
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Презентація #

Цей додаток було створено на прохання учасника поштової конференції додатків
для NVDA.

Він надає комбінацію клавіш NVDA + F4, яка дозволяє отримати інформацію про
поточну мову клавіатури.

Якщо натиснути двічі, повідомляє основну мову системи.

Перша версія цього модуля була простим плагіном, який треба було вставити
вручну до папки з конфігурацією NVDA. Однак тепер його перетворено у
додаток.

## Примітки ##

Якщо клавіатурна команда NVDA + F4 конфліктує з іншою командою, ви можете
змінити її в розділі "Жести вводу", що розташований в підменю "Параметри"
головного меню NVDA.

Після цього ви знайдете сценарій у категорії «Статус системи».

## Сумісність ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

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
