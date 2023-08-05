# Izgovori jezik trenutačne tipkovnice (sayCurrentKeyboardLanguage) #

* Autori: Abdel, Noelia;
* Preuzmi [stabilnu
  verziju](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Preuzmi [razvojnu
  verziju](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Prezentacija #

Ovaj je dodatak izrađen na temelju zahtjeva jednog člana na mailing listi
nvda dodataka.

It provides a script without gesture, which allows to retrieve and give the
language of the current keyboard.

Dvaput pritisnuto, izgovara standardni jezik sustava.

U prvoj verziji je modul bio predložen kao jednostavni globalni dodatak,
kojeg je trebalo zalijepiti u konfiguracijski direktorij za NVDA. Nakon toga
je promijenjen u dodatak.

## Napomene ##

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

## Kompatibilnost ##

* Ovaj je dodatak kompatibilan s NVDA verzijom 2019.3 i novijim verzijama.

## Changes for 20230729.0.0 ##

* Programskom kodu su dodana flake8 i mypy pravila.
* Namjanja podržana NVDA verzija je promijenjena na 2019.3 kako bi se
  podržale zabilješke koje su uvedene u Python 3.
* Removed the "NVDA + F4" gesture calling the script giving the keyboard
  language., to allow users to choose their preferred gesture.

## Promjene u verziji 20230426.0.0 i novije##

* Promijenjen je broj verzije, minimalna NVDA verzija i poveznica za
  preuzimanje, u skladu s konvencijama/zahtjevima trgovine.

## Promjene u verziji 19.02 ##

* Promijenjeno je numeriranje verzija koristeći YY.MM (Dvije znamenke za
  godinu, slijedi točka, a zatim dvije znamenke za mjesec);
* Dodana je kompatibilnost s novim formatom za određivanje verzije dodataka,
  pojavila se u nvda verziji 2019.1.

## Promjene u verziji 1.1 ##

* Dodatak je preimenovan iz „getCurKeyboardLanguage” u
  „sayCurrentKeyboardLanguage”;
* Dodatku je dodana je opća javna licenca;
* U kategoriju „Stanje sustava” dodana je skripta „getCurKeyboardLanguage”
  (Izgovori jezik trenutačne tipkovnice);
* Neki ispravci u kodu.

## Promjene u verziji 1.0 ##

* Prvo izdanje.

[[!tag dev stable]]
