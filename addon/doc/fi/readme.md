# Sano näppäimistön nykyinen kieli #

* Tekijä: Abdel ja Noelia.

# Kuvaus #

Tämä lisäosa tehtiin erään nvda-addons-postituslistan jäsenen pyynnöstä.

Se tarjoaa ilman näppäinkomentoa olevan skriptin, joka ilmoittaa nykyisen
näppäimistökielen.

Kahdesti painettaessa ilmoitetaan järjestelmän oletuskieli.

Ensimmäinen versio oli yksinkertainen NVDA:n asetushakemistoon kopioitava
yleisliitännäinen, mutta myöhemmin se muunnettiin lisäosaksi.

## Huomautuksia ##

Määritä näppäinkomento kielen puhuttavalle skriptille seuraavasti:

* Avaa NVDA-valikko näppäinkomennolla NVDA+N.
* Siirry Asetukset-valikkoon.
* Siirry tämän jälkeen kohtaan "Näppäinkomennot" ja avaa se Enterillä.
* Valitse sitten "Syöttö"-kategoria ja avaa se oikealla nuolinäppäimellä.
* Siirry kohtaan "Ilmoittaa käytössä olevan näppäimistön kielen tai kahdesti
  painettaessa järjestelmän oletuskielen."
* Kun olet valmis, lisää näppäinkomennto painamalla Alt+L ja ppaina sen
  jälkeen NVDA+F4 tai jotain muuta haluamaasi näppäinkomentoa.
* Kun tämä on tehty, paina kerran ylänuolta, jolloin kuulet "<valitsemasi
  näppäinkomento>, kaikki asettelut".
* Hyväksy painamalla Enter, siirry Sarkain-näppäimellä OK-painikkeeseen ja
  paina lopuksi Enter.
* Tämän jälkeen valitsemasi näppäinkomennon pitäisi ilmoittaa näppäimistön
  kielen.

## Yhteensopivuus ##

* Tämä lisäosa on yhteensopiva NVDA 2019.3:n ja sitä uudempien versioiden
  kanssa.

## Muutokset versiossa 20240326.0.0

* Päivitetty yhteensopivuus NVDA 2024.1:lle.
* Latauslinkki poistettu dokumentaatiosta. Tulevien päivitysten latauslinkit
  löytyvät jatkossa vain lisäosakaupasta.

## Muutokset versiossa 20231229.0.0 ##

* Lisätty taaksepäin yhteensopiva toteutus pyydettäessä-puhetilalle, joka on
  käytettävissä NVDA 2024.1:ssä.

## Muutokset versiossa 20230729.0.0 ##

* Sovellettu koodiin flake8- ja mypy-sääntöjä.
* Muutettu NVDA:n tuetuksi vähimmäisversioksi 2019.3 Python 3:ssa
  esiteltyjen selitteiden tukemiseksi.
* Poistettu näppäimistökielen ilmoittava NVDA+F4-näppäinkomento, joka
  mahdollistaa käyttäjille halutun näppäinkomennon valitsemisen.

## Muutokset versiossa 20230426.0.0 ja sitä uudemmissa ##

* Versionumero, NVDA:n vähimmäisversio ja latauslinkki vaihdettu kaupan
  käytäntöjen/vaatimusten mukaisiksi.

## Muutokset versiossa 19.02 ##

* Versionumerointi muutettu muotoon vv.kk (vuosi kahdella numerolla, piste
  ja kuukausi kahdella numerolla);
* Lisätty yhteensopivuus lisäosan uudelle versionumeroinnille, joka otettiin
  käyttöön NVDA 2019.1:stä alkaen.

## Muutokset versiossa 1.1 ##

* Lisäosan uusi nimi on sayCurrentKeyboardLanguage. Vanha:
  getCurKeyboardLanguage;
* Lisätty GPL-lisenssi;
* Lisätty skripti getCurKeyboardLanguage "Järjestelmän tila" -kategoriaan;
* Koodin virheitä korjattu.

## Muutokset versiossa 1.0 ##

* Ensimmäinen versio.

[[!tag dev stable]]
