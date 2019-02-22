# Aktive Tastatursprache ansagen #

* Autoren: Abdel, Noelia;
* Download [stable version][1];
* Download [development version][2].

# Einführung #

Diese Erweiterung wurde auf Anfrage eines Mitglieds der nvda-addons
Mailingliste erstellt.

It provides a keyboard shortcut, NVDA + F4, which allows to retrieve and
give the language of the current keyboard.

Bei zweimaligem Drücken wird die Standardsprache des Systems angesagt.

Bei der ersten Version dieses Moduls war es lediglich ein globales Plugin,
welches in die NVDA-Konfiguration integriert werden musste. Später wurde es
in eine Erweiterung ausgelagert.

## Anmerkungen ##

If the NVDA + F4 keyboard shortcut conflicts with another command, you can
change it by going to the Preferences menu of NVDA, in the "Input gestures"
submenu.

You will then find the script in the "System status" category.

## Kompatibilität ##

* Diese Erweiterung ist kompatibel mit den NVDA-Versionen von 2014.3 bis
  2019.1.

## Changes for version 19.02 ##

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

[1]: https://addons.nvda-project.org/files/get.php?file=ckbl

[2]: https://addons.nvda-project.org/files/get.php?file=ckbl-dev
