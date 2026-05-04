# Изговаряне на текущия език на клавиатурата (sayCurrentKeyboardLanguage)

- Author(s): Abdel, Noelia.

# Представяне

Тази добавка е създадена по желание на член на пощенския списък за добавки
за NVDA.

Тя предоставя скрипт без жест, който позволява да се извлича и докладва
текущият език на клавиатурата.

Ако бъде натисната двукратно, извежда езика по подразбиране на системата.

Първата версия на този модул беше предложен като глобален плъгин, който да
бъде поставян в конфигурационната директория на NVDA, След това беше
преобразуван в добавка.

## Забележки

За да зададете жест към скрипта, докладващ езика на клавиатурата, изпълнете
следните стъпки:

- Отворете менюто на NVDA с NVDA+N;
- Отидете в менюто "Настройки" на NVDA;
- След това отидете на елемента "Жестове на въвеждане" и го задействайте.
- След това изберете категорията "Въвеждане" и я разгънете със стрелка
  надясно.
- Go to the item labeled "Gives the language of the keyboard in use, if pressed twice, give the default language of the system";
- След като сте готови, натиснете Alt+Д, за да добавите жест, и натиснете
  клавишна команда по ваш избор (напр. NVDA+F4);
- След това, натиснете веднъж стрелка нагоре, ще чуете "избраният от вас
  жест, всички клавиатурни подредби";
- Потвърдете с ENTER, след това отидете с TAB до OK, след което натиснете
  ENTER;
- След това избраният от вас жест трябва да извика скрипта, който докладва
  езика на клавиатурата.

## Съвместимост

- Тази добавка е съвместима с версиите на NVDA в диапазона от 2019.3 и
  по-нови.

## Changes for 20240326.0.0

- Updated compatibility for nvda-2024.1.;
- Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0

- Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Промени във версия 20230729.0.0

- Приложени са правилата flake8 и mypy към кода;
- Променена е минималната поддържана версия на NVDA на 2019.3, за да се
  поддържат анотации, въведени в Python 3.
- Премахнат е жестът NVDA+F4, извикващ скрипта, докладващ езика на
  клавиатурата, за да позволи на потребителите да изберат предпочитания от
  тях жест.

## Промени във версия 20230426.0.0 and beyond#\#

- Променени са номера на версията, минималната версия на NVDA и връзката за
  изтегляне според конвенциите/изискванията на магазина.
- auto-update-translations - to automatically update translations from NVDA's translation system.
- release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
- manual-release.yaml: to build and release new versions of the add-on manually.
- Updated translations.

## Промени във версия 19.02

- Променено е номерирането на версията – сега тя се формира във формата
  ГГ.ММ (годината в 2 цифри, последвана от точка, последвана от номера на
  месеца с 2 цифри).

## Промени във версия 1.1

- Добавката беше преименувана от "Получаване на текущия език на
  клавиатурата" на "Изговаряне на текущия език на клавиатурата".
- Добавен е GPL лиценза към добавката;

## Промени във версия 1.0

- Първо издание.
- Added the GPL license to the addon;
- Added the script getCurKeyboardLanguage to the "System status" category;
- Fixed some errors in the code.

## Changes for version 1.0

- Initial version.
