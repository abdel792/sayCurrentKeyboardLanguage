# Izgovori jezik trenutačne tipkovnice (sayCurrentKeyboardLanguage) #

* Autori: Abdel, Noelia;
* Preuzmi [stabilnu verziju][1]

# Prezentacija #

Ovaj je dodatak izrađen na temelju zahtjeva jednog člana na mailing listi
nvda dodataka.

Dodatak koristi tipkovnički prečac NVDA+F4, pomoću kojeg se pronalazi i
izgovara jezik trenutačne tipkovnice.

Dvaput pritisnuto, izgovara standardni jezik sustava.

U prvoj verziji je modul bio predložen kao jednostavni globalni dodatak,
kojeg je trebalo zalijepiti u konfiguracijski direktorij za NVDA. Nakon toga
je promijenjen u dodatak.

## Napomene ##

Ako se tipkovnički prečac NVDA+F4 sukobljava s nekom drugom naredbom, može
se promijeniti u NVDA izborniku „Postavke”, u podizborniku „Ulazne geste”.

Skripta se nalazi u kategoriji „Stanje sustava”.

## Kompatibilnost ##

* Ovaj je dodatak kompatibilan s NVDA 2014.3 i novijim verzijama.

## Promjene u verziji 20230426.0.0 ##

* Promijenjen je broj verzije, minimalna NVDA verzija i poveznica za
  preuzimanje, u skladu s konvencijama/zahtjevima trgovine.
* Kompatibilno s NVDA 2023.1 i novijim verzijama.

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

[1]:
https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage
