# sayCurrentKeyboardLanguage #

* Autorzy: Abdel, Noelia;
* Download [stable
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Download [development
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Prezentacja #

Ten dodatek został utworzony na prośbę członka listy mailingowej
nvda-addons.

It provides a script without gesture, which allows to retrieve and give the
language of the current keyboard.

Dwukrotne naciśnięcie powoduje podanie domyślnego języka systemu.

W pierwszej wersji modułu, został on zaproponowany jako globalna wtyczka
dlaNVDA, potem był on przekształcony w pakiet addon.

## Uwagi ##

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

## Zgodność ##

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

## Zmiany w wersji 19.02 ##

* Zmieniono numerację wersji przy użyciu YY. MM (Rok w 2 cyfrach, po którym
  następuje kropka, a następnie miesiąc w 2 cyfrach);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Zmiany dla wersji 1.1 ##

* Nazwa dodatku została zmieniona z getCurKeyboardLanguage na
  sayCurrentKeyboardLanguage;
* Dodano licencję GPL;
* Dodano skrypt getCurKeyboardLanguage do kategorii "Stan systemu";
* Poprawione niektóre błędy w kodzie.

## Zmiany dla wersji 1.0 ##

* Wersja pierwotna.

[[!tag dev stable]]
