# sayCurrentKeyboardLanguage #

* Autor(es): Abdel, Noelia;
* Download [stable
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Download [development
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Presentación #

Este complemento creouse seguindo unha petición dun membro da lista de
correo de complementos do NVDA.

It provides a script without gesture, which allows to retrieve and give the
language of the current keyboard.

Se se preme dúas veces, da a lingua predeterminada do sistema.

Na primeira versión deste módulo, propuxérase coma un sinxelo plugin global
para pegar no directorio de configuración do NVDA, entón transformouse nun
complemento.

## Notas ##

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

## Compatibilidade ##

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

## Cambios para a versión 19.02 ##

* Cambiado o numerado de versións utilizando YY.MM (O ano en dous díxitos,
  seguido dun punto, seguido do mes en dous díxitos);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Cambios para a versión 1.1 ##

* O complemento renomeouse de getCurKeyboardLanguage a
  sayCurrentKeyboardLanguage;
* Engadida a licenza GPL ao complemento;
* Engadido o script getCurKeyboardLanguage á categoría "Estado do Sistema";
* Arranxados algúns erros no código.

## Cambios para a versión 1.0 ##

* Versión inicial.

[[!tag dev stable]]
