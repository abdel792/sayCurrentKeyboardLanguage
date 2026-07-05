# sayCurrentKeyboardLanguage

* Tekijä(t): Abdel, Noelia.

# Esittely #

Tämä lisäosa luotiin nvda-addons-sähköpostilistan jäsenen pyynnöstä.

Se tarjoaa skriptin ilman pikanäppäintä, jonka avulla voidaan hakea ja ilmoittaa nykyisen näppäimistön kieli.

Kaksi kertaa painettaessa se ilmoittaa järjestelmän oletuskielen.

Tämän moduulin ensimmäisessä versiossa sitä ehdotettiin yksinkertaisena globalPlugin-liitännäisenä liitettäväksi NVDA-asetushakemistoon, minkä jälkeen se muutettiin lisäosaksi.

## Huomautukset ##

Asettaaksesi pikanäppäimen näppäimistön kielen ilmoittavalle skriptille, toimi seuraavasti:

* Avaa NVDA-valikko näppäinyhdistelmällä "NVDA + N";
* Siirry NVDA:n Asetukset-valikkoon;
* Siirry sen jälkeen "Syötteet"-alivalikkoon.
* Valitse sitten kategoria "Syöte" ja avaa se oikealla nuolella.
* Siirry kohtaan, jonka otsikko on "Ilmoittaa käytössä olevan näppäimistön kielen, kaksi kertaa painettaessa ilmoittaa järjestelmän oletuskielen";
* Kun tämä on tehty, paina Alt + A lisätäksesi pikanäppäimen ja näppäile "NVDA + F4" tai jokin muu valitsemasi näppäinyhdistelmä;
* Tämän jälkeen paina ylänuolta kerran, jolloin kuulet "valitsemasi pikanäppäin, kaikki näppäinasettelut";
* Vahvista painamalla Enter, siirry sitten Tab-näppäimellä OK-painikkeeseen ja paina Enter;
* Valitsemasi pikanäppäimen pitäisi nyt kutsua näppäimistön kielen ilmoittavaa skriptiä.

## Yhteensopivuus ##

* Tämä lisäosa on yhteensopiva NVDA-versioiden 2019.3 ja sitä uudempien kanssa.

## Muutokset versiossa 20240326.0.0

* Päivitetty yhteensopivuus nvda-2024.1-versiolle;
* Latauslinkki poistettu readme-tiedostosta, tulevien päivitysten latauslinkki on jatkossa saatavilla vain lisäosakaupasta.

## Muutokset versiossa 20231229.0.0 ##

* Lisätty taaksepäin yhteensopiva toteutus tukemaan puhetta tarvittaessa -tilaa, joka on pian saatavilla nvda-2024.1-version myötä.

## Muutokset versiossa 20230729.0.0 ##

* Sovellettu flake8- ja mypy-sääntöjä koodiin;
* Muutettu pienin tuettu NVDA-versio versioksi 2019.3 Python 3:ssa esiteltyjen tyyppivihjeiden tukemiseksi.
* Poistettu näppäimistön kielen ilmoittavaa skriptiä kutsuva pikanäppäin "NVDA + F4", jotta käyttäjät voivat valita haluamansa pikanäppäimen.

## Muutokset versiossa 20230607.0.0 ##

* Lisätty seuraavat työnkulut:
 * auto-update-translations - käännösten automaattiseen päivittämiseen NVDA:n käännösjärjestelmästä.
 * release-on-tag..yaml: lisäosan kääntämiseen ja julkaisemiseen heti, kun uusi tagi pushetaan;
 * manual-release.yaml: uusien lisäosaversioiden manuaaliseen kääntämiseen ja julkaisemiseen.
* Päivitetty käännökset.

## Muutokset versiossa 20230426.0.0 ja sitä uudemmissa ##

* • Muutettu versionumero, NVDA:n vähimmäisversio ja latauslinkki kaupan käytäntöjen/vaatimusten mukaisesti.

## Muutokset versiossa 19.02 ##

* Muutettu versionumerointi muotoon VV.KK (vuosi kahdella digiitillä, jota seuraa piste, jota seuraa kuukausi kahdella digiitillä);
* Lisätty yhteensopivuus lisäosien uuden versionumerointimuodon kanssa, joka tuli käyttöön nvda 2019.1 -versiosta alkaen.

## Muutokset versiossa 1.1 ##

* Lisäosan nimi on muutettu muodosta getCurKeyboardLanguage muotoon sayCurrentKeyboardLanguage;
* Lisätty GPL-lisenssi lisäosaan;
* Lisätty skripti getCurKeyboardLanguage kategoriaan "Järjestelmän tila";
* Korjattu joitakin virheitä koodissa.

## Muutokset versiossa 1.0 ##

* Ensimmäinen versio.
