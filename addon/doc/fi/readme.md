# Sano näppäimistön nykyinen kieli #

* Tekijät: Abdel, Noelia;
* Lataa [vakaa versio][1];
* Lataa [kehitysversio][2].

# Kuvaus #

Tämä lisäosa tehtiin erään nvda-addons-postituslistan jäsenen pyynnöstä.

Se tarjoaa näppäinkomennon NVDA+F4, joka ilmoittaa nykyisen näppäinasettelun
kielen.

Kahdesti painettaessa ilmoitetaan järjestelmän oletuskieli.

Ensimmäinen versio oli yksinkertainen NVDA:n asetushakemistoon kopioitava
yleisliitännäinen, mutta myöhemmin se muunnettiin lisäosaksi.

## Huomautuksia ##

Mikäli pikanäppäin NVDA+F4 on ristiriidassa jonkin toisen komennon kanssa,
voit muuttaa sitä menemällä NVDA:n Asetukset-valikkoon ja valitsemalla
"Näppäinkomennot"-vaihtoehdon.

Lisäosan komento löytyy tämän jälkeen "Järjestelmän tila" -kategoriasta.

## Yhteensopivuus ##

* NVDA:n versiot 2014.3-2019.3 ovat yhteensopivia tämän lisäosan kanssa.

## Muutokset versiossa 19.02 ##

* Versionumerointi muutettu muotoon vv.kk (vuosi kahdella numerolla, piste
  ja kuukausi kahdella numerolla);
* Lisätty yhteensopivuus lisäosan uudelle versionumeroinnille, joka otettiin
  käyttöön NVDA 2019.1:ssä.

## Muutokset versiossa 1.1 ##

* Lisäosan uusi nimi on sayCurrentKeyboardLanguage. Vanha:
  getCurKeyboardLanguage;
* Lisätty GPL-lisenssi;
* Lisätty skripti getCurKeyboardLanguage "Järjestelmän tila" -kategoriaan;
* Koodin virheitä korjattu.

## Muutokset versiossa 1.0 ##

* Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=ckbl

[2]: https://www.nvaccess.org/addonStore/legacy?file=ckbl-dev
