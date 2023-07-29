# Aktive Tastatursprache ansagen #

* Autoren: Abdel, Noelia;
* [Stabile Version
  herunterladen](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* [Entwicklerversion
  herunterladen](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Einführung #

Diese Erweiterung wurde auf Anfrage eines Mitglieds der nvda-addons
Mailingliste erstellt.

Diese Erweiterung  stellt eine Tastenkombination (NVDA+F4) zur Verfügung,
welche die Informationen zum verwendeten Tastaturlayout mitteilt.

Bei zweimaligem Drücken wird die Standardsprache des Systems angesagt.

Bei der ersten Version dieses Moduls war es lediglich ein globales Plugin,
welches in die NVDA-Konfiguration integriert werden musste. Später wurde es
in eine Erweiterung ausgelagert.

## Anmerkungen ##

Falls die Tastenkombination NVDA+F4 mit einer anderen Tastenkombination
kollidieren sollte, können Sie sie in den NVDA-Einstellungen im Untermenü
"Eingaben" anpassen.

Sie finden den Befehl in der Kategorie "Systemstatus".

## Kompatibilität ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

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
