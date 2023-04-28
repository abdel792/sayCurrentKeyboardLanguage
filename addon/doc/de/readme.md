# Aktive Tastatursprache ansagen #

* Autoren: Abdel, Noelia;
* Download [stable version][1]

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

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  and beyond.

## Changes for version 20230426.0.0 ##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.
* Compatible with NVDA2023.1 and beyond.

## Änderungen in Version 19.02 ##

* Die Versionsnummerierung wurde mit JJ.MM geändert (das Jahr in 2 Ziffern,
  gefolgt von einem Punkt, gefolgt von dem Monat in 2 Ziffern);
* Die Kompatibilität mit dem neuen Versionierungsformat der Erweiterung
  wurde gesichert, erschienen seit nvda 2019.1.

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

[1]:
https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage
