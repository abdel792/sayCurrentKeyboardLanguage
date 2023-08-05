# Vyslov jazyk klávesnice #

* Autorii: Abdel, Noelia;
* Download [stable
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Download [development
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Prezentácia #

Doplnok bol vytvorený ako reakcia na požiadavku jedného člena komunity.

It provides a script without gesture, which allows to retrieve and give the
language of the current keyboard.

Stlačené dvakrát rýchlo za sebou oznámi jazyk systému.

Pôvodne išlo len o globálny plugin, ktorýu bolo potrebné pre jeho správnu
funkčnosť skopírovať do adresára s nastaveniami a konfiguráciou NVDA, neskôr
bol prerobený na doplnok.

## Poznámky ##

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

## Kompatibilita ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230729.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.
* Removed the "NVDA + F4" gesture calling the script giving the keyboard
  language., to allow users to choose their preferred gesture.

## Changes for version 20230426.0.0 and beyond##

* Upravené číslovanie verzie, posledná verzia NVDA kompatibilná s doplnkom
  podľa odporúčaní.

## Verzia 19.02 ##

* Zmenené číslovanie verzií. Teraz sa používa systém yy.mm (dve číslice pre
  rok a dve pre mesiac);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Verzia 1.1 ##

* Doplnok premenovaný z getCurKeyboardLanguage na sayCurrentKeyboardLanguage
  (anglicky);
* Pridaná GPL licencia;
* Pridaná skratka do kategórie systém;
* Opravené chyby v kóde.

## Verzia 1.0 ##

* Prvé vydanie.

[[!tag dev stable]]
