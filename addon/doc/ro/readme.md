# sayCurrentKeyboardLanguage

* Autor(i): Abdel, Noelia.

# Prezentare #

Acest supliment a fost creat la cererea unui membru de pe lista de discuții nvda-addons.

Acesta oferă un script fără gest, care permite preluarea și anunțarea limbii tastaturii curente.

Dacă este apăsat de două ori, anunță limba implicită a sistemului.

La prima versiune a acestui modul, el a fost propus ca un simplu globalPlugin care trebuia lipit în directorul de configurare al NVDA, fiind apoi transformat în supliment.

## Note ##

Pentru a seta un gest pentru scriptul care anunță limba tastaturii, urmați acești pași:

* Deschideți meniul NVDA cu "NVDA + N";
* Mergeți la meniul de preferințe al NVDA;
* Apoi mergeți la submeniul "Geste de intrare".
* Apoi selectați categoria "Introducere" și deschideți-o cu săgeată dreapta.
* Mergeți la elementul etichetat "Anunță limba tastaturii utilizate, dacă este apăsat de două ori, anunță limba implicită a sistemului";
* Odată ce ați făcut acest lucru, apăsați Alt + A pentru a adăuga un gest și tastați "NVDA + F4" sau un alt gest la alegere;
* După aceasta, apăsați o dată săgeata în sus, veți auzi „gestul ales de dvs., toate aranjamentele”;
* Validați cu Enter, apoi mergeți cu Tab la OK și apăsați Enter;
* Gestul ales ar trebui apoi să apeleze scriptul care anunță limba tastaturii.

## Compatibilitate ##

* Acest supliment este compatibil cu versiunile NVDA cuprinse între 2019.3 și ulterioare.

## Modificări pentru 20240326.0.0

* S-a actualizat compatibilitatea pentru nvda-2024.1;
* S-a șters linkul de descărcare din readme, linkul de descărcare pentru actualizările viitoare va fi acum disponibil doar în magazinul de suplimente.

## Modificări pentru 20231229.0.0 ##

* S-a adăugat o implementare compatibilă cu versiunile anterioare pentru a asigura suportul pentru modul de vorbire la cerere, care va fi disponibil în curând cu nvda-2024.1.

## Modificări pentru 20230729.0.0 ##

* S-au aplicat regulile flake8 și mypy asupra codului;
* S-a schimbat versiunea minimă acceptată de NVDA la 2019.3 pentru a accepta adnotările introduse în Python 3.
* S-a eliminat gestul "NVDA + F4" care apela scriptul ce anunța limba tastaturii, pentru a permite utilizatorilor să își aleagă gestul preferat.

## Modificări pentru 20230607.0.0 ##

* S-au adăugat următoarele fluxuri de lucru:
 * auto-update-translations - pentru a actualiza automat traducerile din sistemul de traducere al NVDA.
 * release-on-tag..yaml: pentru a construi și publica suplimentul de îndată ce este trimis un nou tag;
 * manual-release.yaml: pentru a construi și lansa manual noi versiuni ale suplimentului.
* S-au actualizat traducerile.

## Modificări pentru versiunea 20230426.0.0 și ulterioare ##

* • S-au schimbat numărul versiunii, versiunea minimă de NVDA și linkul de descărcare în conformitate cu convențiile/cerințele magazinului.

## Modificări pentru versiunea 19.02 ##

* S-a schimbat numerotarea versiunilor folosind formatul AA.LL (anul din 2 cifre, urmat de punct, urmat de luna din 2 cifre);
* S-a adăugat compatibilitatea cu noul format de numerotare a versiunilor pentru suplimente, apărut începând cu nvda 2019.1.

## Modificări pentru versiunea 1.1 ##

* Suplimentul a fost redenumit din getCurKeyboardLanguage în sayCurrentKeyboardLanguage;
* S-a adăugat licența GPL la supliment;
* S-a adăugat scriptul getCurKeyboardLanguage în categoria „Starea sistemului”;
* S-au corectat unele erori din cod.

## Modificări pentru versiunea 1.0 ##

* Versiunea inițială.
