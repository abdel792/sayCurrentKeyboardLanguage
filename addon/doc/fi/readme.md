# Sano näppäimistön nykyinen kieli #

* Tekijät: Abdel, Noelia;
* Lataa [vakaa
  versio](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Lataa
  [kehitysversio](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

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

* Tämä lisäosa on yhteensopiva NVDA 2019.3:n ja sitä uudempien versioiden
  kanssa.

## Muutokset versiossa 20230728.0.0 ##

* Sovellettu koodiin flake8- ja mypy-sääntöjä.
* Muutettu NVDA:n tuetuksi vähimmäisversioksi 2019.3 Python 3:ssa
  esiteltyjen selitteiden tukemiseksi.

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
