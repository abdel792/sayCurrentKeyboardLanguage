# sayCurrentKeyboardLanguage

* Autor(i): Abdel, Noelia.

# Prezentácia #

Doplnok bol vytvorený na základe požiadavky člena v e-mailovej konferencii nvda-addons.

Poskytuje skript bez priradeného gesta, ktorý umožňuje zistiť a oznámiť jazyk aktuálnej klávesnice.

Ak sa stlačí dvakrát, oznámi predvolený jazyk systému.

V prvej verzii tohto modulu bol navrhnutý ako jednoduchý globalPlugin na vloženie do konfiguračného adresára NVDA, následne bol transformovaný na doplnok.

## Poznámky ##

Ak chcete skriptu na oznamovanie jazyka klávesnice priradiť gesto, postupujte takto:

* Otvorte ponuku NVDA pomocou "NVDA + N";
* Prejdite do ponuky nastavení NVDA;
* Potom prejdite do podponuky "Vstupné gestá".
* Následne vyberte kategóriu "Vstup" a otvorte ju šípkou doprava.
* Prejdite na položku s názvom "Oznamuje jazyk používanej klávesnice, ak sa stlačí dvakrát, oznámi predvolený jazyk systému";
* Po dokončení stlačte Alt + A na pridanie gesta a zadajte "NVDA + F4" alebo iné gesto podľa vášho výberu;
* Po vykonaní tohto kroku stlačte raz šípku nahor, budete počuť „vaše zvolené gesto, všetky rozloženia“;
* Potvrďte stlačením klávesu Enter, potom prejdite tabulátorom na tlačidlo OK a stlačte Enter;
* Vaše zvolené gesto by potom malo vyvolať skript, ktorý oznamuje jazyk klávesnice.

## Kompatibilita ##

* Tento doplnok je kompatibilny s verziami NVDA od 2019.3 a novšími.

## Zmeny pre 20240326.0.0

* Aktualizovaná kompatibilita pre nvda-2024.1;
* Odstránený odkaz na stiahnutie z readme, odkaz na stiahnutie pre budúce aktualizácie bude odteraz dostupný iba v obchode s doplnkami.

## Zmeny pre 20231229.0.0 ##

* Pridaná spätne kompatibilná implementácia na podporu režimu reči na požiadanie, ktorý bude čoskoro dostupný v nvda-2024.1.

## Zmeny pre 20230729.0.0 ##

* Na kód sa aplikovali pravidlá flake8 a mypy;
* Zmenená minimálna podporovaná verzia NVDA na 2019.3 kvôli podpore anotácií zavedených v Pythone 3.
* Odstránené gesto "NVDA + F4", ktoré vyvolávalo skript na oznamovanie jazyka klávesnice, aby si používatelia mohli vybrať vlastné preferované gesto.

## Zmeny pre 20230607.0.0 ##

* Pridané nasledujúce pracovné postupy (workflows):
 * auto-update-translations - pre automatickú aktualizáciu prekladov z prekladateľského systému NVDA.
 * release-on-tag..yaml: na zostavenie a publikovanie doplnku hneď po odoslaní nového tagu;
 * manual-release.yaml: na manuálne zostavenie a vydávanie nových verzií doplnku.
* Aktualizované preklady.

## Zmeny pre verziu 20230426.0.0 a novšie ##

* • Zmenené číslo verzie, minimálna verzia NVDA a odkaz na stiahnutie podľa konvencií/požiadaviek obchodu.

## Zmeny pre verziu 19.02 ##

* Zmenené číslovanie verzií pomocou formátu RR.MM (rok v 2 čísliciach, za ktorým nasleduje bodka, za ktorou nasleduje mesiac v 2 čísliciach);
* Pridaná kompatibilita s novým formátom číslovania verzií doplnkov, ktorý sa objavil od nvda 2019.1.

## Zmeny pre verziu 1.1 ##

* Doplnok bol premenovaný z getCurKeyboardLanguage na sayCurrentKeyboardLanguage;
* Do doplnku bola pridaná licencia GPL;
* Pridaný skript getCurKeyboardLanguage do kategórie "Stav systému";
* Opravené niektoré chyby v kóde.

## Zmeny pre verziu 1.0 ##

* Počiatočná verzia.
