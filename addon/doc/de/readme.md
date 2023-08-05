# Aktive Tastatursprache ansagen #

* Autoren: Abdel, Noelia;
* [Stabile Version
  herunterladen](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* [Entwicklerversion
  herunterladen](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Einführung #

Diese Erweiterung wurde auf Anfrage eines Mitglieds der nvda-addons
Mailingliste erstellt.

It provides a script without gesture, which allows to retrieve and give the
language of the current keyboard.

Bei zweimaligem Drücken wird die Standardsprache des Systems angesagt.

Bei der ersten Version dieses Moduls war es lediglich ein globales Plugin,
welches in die NVDA-Konfiguration integriert werden musste. Später wurde es
in eine Erweiterung ausgelagert.

## Anmerkungen ##

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

## Kompatibilität ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230729.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.
* Removed the "NVDA + F4" gesture calling the script giving the keyboard
  language., to allow users to choose their preferred gesture.

## Änderungen in Version 20230426.0.0 und neuer

* Die Versionsnummer, die minimale NVDA-Version und der Download-Link wurden
  entsprechend den Konventionen bzw. der Anforderungen für den Store für
  NVDA-Erweiterungen geändert.

## Änderungen in Version 19.02 ##

* Die Versionsnummerierung wurde mit JJ.MM geändert (das Jahr in 2 Ziffern,
  gefolgt von einem Punkt, gefolgt von dem Monat in 2 Ziffern);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Änderungen in Version 1.1 ##

* Die Erweiterung wurde von "getCurKeyboardLanguage" in
  "sayCurrentKeyboardLanguage" umbenannt;
* Die GPL-Lizenz wurde zur Erweiterung hinzugefügt;
* Das Skript "getCurKeyboardLanguage" wurde zur Kategorie "System status"
  hinzugefügt;
* Einige Fehler im code wurden behoben.

## Änderungen in Version 1.0 ##

* Erste Version.

[[!tag dev stable]]
