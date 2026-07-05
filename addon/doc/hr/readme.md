# sayCurrentKeyboardLanguage

* Autor(i): Abdel, Noelia.

# Predstavljanje #

Ovaj dodatak je kreiran na zahtjev člana s nvda-addons dopisne liste.

Pruža skriptu bez dodijeljene geste koja omogućuje dohvaćanje i izgovaranje jezika trenutne tipkovnice.

Ako se pritisne dvaput, daje zadani jezik sustava.

U prvoj verziji ovog modula, bio je predložen kao jednostavan globalPlugin koji se lijepi u konfiguracijsku mapu NVDA-a, a zatim je transformiran u dodatak.

## Napomene ##

Za postavljanje geste za skriptu koja daje jezik tipkovnice, slijedite ove korake:

* Otvorite NVDA izbornik pomoću "NVDA + N";
* Idite na izbornik postavki NVDA-a;
* Zatim idite na podizbornik "Ulazne geste".
* Zatim odaberite kategoriju "Unos" i otvorite je desnom strelicom.
* Idite na stavku s oznakom "Daje jezik tipkovnice u upotrebi, ako se pritisne dvaput, daje zadani jezik sustava";
* Nakon što to učinite, pritisnite Alt + A za dodavanje geste i upišite "NVDA + F4" ili neku drugu gestu po vašem izboru;
* Nakon toga pritisnite strelicu prema gore jednom, čut ćete "vaša odabrana gesta, svi rasporedi";
* Potvrdite pritiskom na Enter, zatim tabulatorom idite do U redu i pritisnite Enter;
* Vaša odabrana gesta trebala bi tada pozvati skriptu koja daje jezik tipkovnice.

## Kompatibilnost ##

* Ovaj dodatak je kompatibilan s verzijama NVDA od 2019.3 i novijim.

## Promjene za 20240326.0.0

* Ažurirana kompatibilnost za nvda-2024.1;
* Izbrisana poveznica za preuzimanje iz readme datoteke, poveznica za preuzimanje za buduća ažuriranja sada će biti dostupna samo u trgovini dodataka.

## Promjene za 20231229.0.0 ##

* Dodana implementacija kompatibilna s prethodnim verzijama za podršku načina govora na zahtjev, koji će uskoro biti dostupan s nvda-2024.1.

## Promjene za 20230729.0.0 ##

* Primijenjena pravila flake8 i mypy na kod;
* Promijenjena minimalna podržana verzija NVDA-a na 2019.3 radi podrške za anotacije uvedene u Pythonu 3.
* Uklonjena gesta "NVDA + F4" koja poziva skriptu koja daje jezik tipkovnice, kako bi se korisnicima omogućilo da sami odaberu željenu gestu.

## Promjene za 20230607.0.0 ##

* Dodani su sljedeći tijekovi rada:
 * auto-update-translations - za automatsko ažuriranje prijevoda iz NVDA sustava za prevođenje.
 * release-on-tag..yaml: za izradu i objavljivanje dodatka čim se gurne nova oznaka;
 * manual-release.yaml: za ručnu izradu i izdavanje novih verzija dodatka.
* Ažurirani prijevodi.

## Promjene za verziju 20230426.0.0 i novije ##

* • Promijenjen broj verzije, minimalna verzija NVDA-a i poveznica za preuzimanje u skladu s konvencijama/zahtjevima trgovine.

## Promjene za verziju 19.02 ##

* Promijenjeno numeriranje verzija pomoću formata GG.MM (godina u 2 znamenke, nakon koje slijedi točka, nakon koje slijedi mjesec u 2 znamenke);
* Dodana kompatibilnost s novim formatom numeriranja verzija dodataka, koji se pojavio od nvda 2019.1.

## Promjene za verziju 1.1 ##

* Dodatak je preimenovan iz getCurKeyboardLanguage u sayCurrentKeyboardLanguage;
* Dodana GPL licenca dodatku;
* Dodana skripta getCurKeyboardLanguage u kategoriju "Status sustava";
* Ispravljene neke pogreške u kodu.

## Promjene za verziju 1.0 ##

* Početna verzija.
