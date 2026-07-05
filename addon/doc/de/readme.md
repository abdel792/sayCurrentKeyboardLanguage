# sayCurrentKeyboardLanguage

* Autor(en): Abdel, Noelia.

# Vorstellung #

Dieses Add-on wurde auf Anfrage eines Mitglieds der nvda-addons-Mailingliste erstellt.

Es stellt ein Skript ohne zugewiesene Geste bereit, mit dem die Sprache der aktuellen Tastatur abgerufen und angesagt werden kann.

Wird es zweimal gedrückt, wird die Standardsprache des Systems ausgegeben.

In der ersten Version dieses Moduls wurde es als einfaches globalPlugin zum Einfügen in das Konfigurationsverzeichnis von NVDA vorgeschlagen, danach wurde es in ein Add-on umgewandelt.

## Hinweise ##

Um dem Skript, das die Tastatursprache ausgibt, eine Geste zuzuweisen, gehen Sie wie folgt vor:

* Öffnen Sie das NVDA-Menü mit "NVDA + N";
* Rufen Sie das Einstellungen-Menü von NVDA auf;
* Gehen Sie dann in das Untermenü "Eingaben";
* Wählen Sie dann die Kategorie "Eingabe" und öffnen Sie diese mit dem Pfeil nach rechts;
* Gehen Sie zu dem Element mit der Beschriftung "Gibt die Sprache der verwendeten Tastatur aus. Wird es zweimal gedrückt, wird die Standardsprache des Systems ausgegeben";
* Drücken Sie anschließend Alt + H, um eine Geste hinzuzufügen, und geben Sie "NVDA + F4" oder eine andere Geste Ihrer Wahl ein;
* Drücken Sie danach einmal die Pfeiltaste nach oben, Sie hören "Ihre gewählte Geste, alle Tastaturlayouts";
* Bestätigen Sie mit der Eingabetaste, wechseln Sie dann mit der Tabulatortaste zu OK und drücken Sie die Eingabetaste;
* Die von Ihnen gewählte Geste sollte nun das Skript aufrufen, das die Tastatursprache ausgibt.

## Kompatibilität ##

* Dieses Add-on ist mit den NVDA-Versionen ab 2019.3 und höher kompatibel.

## Änderungen für 20240326.0.0

* Kompatibilität für nvda-2024.1 aktualisiert;
* Download-Link aus der Readme gelöscht, der Download-Link für zukünftige Updates wird nun nur noch über den Add-on-Store verfügbar sein.

## Änderungen für 20231229.0.0 ##

* Abwärtskompatible Implementierung zur Unterstützung des Modus "Sprache auf Abruf" hinzugefügt, der bald mit nvda-2024.1 verfügbar sein wird.

## Änderungen für 20230729.0.0 ##

* Die flake8- und mypy-Regeln wurden auf den Code angewendet;
* Die minimal unterstützte NVDA-Version wurde auf 2019.3 geändert, um die in Python 3 eingeführten Annotationen zu unterstützen;
* Die Geste "NVDA + F4" zum Aufrufen des Skripts für die Tastatursprache wurde entfernt, damit die Benutzer ihre bevorzugte Geste selbst wählen können.

## Änderungen für 20230607.0.0 ##

* Folgende Workflows wurden hinzugefügt:
 * auto-update-translations - zur automatischen Aktualisierung von Übersetzungen aus dem NVDA-Übersetzungssystem.
 * release-on-tag..yaml: zum Erstellen und Veröffentlichen des Add-ons, sobald ein neuer Tag gepusht wird;
 * manual-release.yaml: zum manuellen Erstellen und Veröffentlichen neuer Versionen des Add-ons.
* Übersetzungen aktualisiert.

## Änderungen für Version 20230426.0.0 und höher ##

* • Versionsnummer, minimale NVDA-Version und Download-Link entsprechend den Konventionen/Anforderungen des Stores geändert.

## Änderungen für Version 19.02 ##

* Versionsnummerierung auf JJ.MM geändert (Das Jahr zweistellig, gefolgt von einem Punkt, gefolgt vom Monat zweistellig);
* Kompatibilität mit dem neuen Format für die Versionsnummerierung von Add-ons hinzugefügt, das seit nvda 2019.1 existiert.

## Änderungen für Version 1.1 ##

* Das Add-on wurde von getCurKeyboardLanguage in sayCurrentKeyboardLanguage umbenannt;
* GPL-Lizenz zum Add-on hinzugefügt;
* Das Skript getCurKeyboardLanguage wurde zur Kategorie "Systemstatus" hinzugefügt;
* Einige Fehler im Code wurden behoben.

## Änderungen für Version 1.0 ##

* Erste Version.
