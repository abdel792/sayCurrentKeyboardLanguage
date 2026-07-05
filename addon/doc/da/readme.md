# sayCurrentKeyboardLanguage

* Forfatter(e): Abdel, Noelia.

# Præsentation #

Dette tilføjelsessprog blev oprettet efter anmodning fra et medlem på nvda-addons-postlisten.

Det giver et script uden genvejstast, som gør det muligt at hente og angive sproget for det aktuelle tastatur.

Hvis der trykkes to gange, angives systemets standardsprog.

I den første version af dette modul blev det foreslået som et simpelt globalPlugin, der skulle indsættes i konfigurationsmappen for NVDA, og det blev derefter omdannet til et tilføjelsessprog.

## Bemærkninger ##

Følg disse trin for at indstille en genvejstast til scriptet, der angiver tastatursproget:

* Åbn NVDA-menuen med "NVDA + N";
* Gå til NVDA's indstillingsmenu;
* Gå derefter til undermenuen "Inputgenveje".
* Vælg derefter kategorien "Input", og åbn den med højre pil.
* Gå til punktet mærket "Giver sproget for det tastatur, der er i brug, hvis der trykkes to gange, gives systemets standardsprog";
* Når det er gjort, skal du trykke på Alt + A for at tilføje en genvej og skrive "NVDA + F4" eller en anden genvej efter eget valg;
* Når dette er gjort, skal du trykke på pil op én gang, og du vil høre "din valgte genvej, alle layouter";
* Bekræft med Enter, og brug derefter Tab til at gå til OK og tryk på Enter;
* Den valgte genvej skal derefter kalde scriptet, der angiver tastatursproget.

## Kompatibilitet ##

* Dette tilføjelsessprog er kompatibelt med versioner af NVDA fra 2019.3 og opefter.

## Ændringer for 20240326.0.0

* Opdateret kompatibilitet for nvda-2024.1;
* Downloadlink slettet fra readme, downloadlinket til fremtidige opdateringer vil nu kun være tilgængeligt fra tilføjelsesbutikken.

## Ændringer for 20231229.0.0 ##

* Tilføjet en bagudkompatibel implementering til at understøtte tale-on-demand-tilstand, som snart vil være tilgængelig med nvda-2024.1.

## Ændringer for 20230729.0.0 ##

* Anvendt flake8- og mypy-reglerne på koden;
* Ændret den mindste understøttede NVDA-version til 2019.3 for at understøtte annotationer introduceret i Python 3.
* Fjernet genvejen "NVDA + F4", der kalder scriptet, som angiver tastatursproget, for at give brugerne mulighed for at vælge deres foretrukne genvej.

## Ændringer for 20230607.0.0 ##

* Tilføjet følgende arbejdsgange:
 * auto-update-translations - til automatisk at opdatere oversættelser fra NVDA's oversættelsessystem.
 * release-on-tag..yaml: til at bygge og udgive tilføjelsessproget, så snart et nyt tag pushes;
 * manual-release.yaml: til at bygge og udgive nye versioner af tilføjelsessproget manuelt.
* Opdaterede oversættelser.

## Ændringer for version 20230426.0.0 og opefter ##

* • Ændret versionsnummer, minimum NVDA-version og downloadlink i henhold til butikkens konventioner/krav.

## Ændringer for version 19.02 ##

* Ændret versionsnummerering ved hjælp af YY.MM (Året med 2 cifre, efterfulgt af et punktum, efterfulgt af måneden med 2 cifre);
* Tilføjet kompatibilitet med det nye versionsformat for tilføjelsessprog, som har været tilgængeligt siden nvda 2019.1.

## Ændringer for version 1.1 ##

* Tilføjelsessproget er blevet omdøbt fra getCurKeyboardLanguage til sayCurrentKeyboardLanguage;
* Tilføjet GPL-licensen til tilføjelsessproget;
* Tilføjet scriptet getCurKeyboardLanguage til kategorien "Systemstatus";
* Rettede nogle fejl i koden.

## Ændringer for version 1.0 ##

* Første version.
