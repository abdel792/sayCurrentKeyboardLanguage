# sayCurrentKeyboardLanguage #

* Autori: Abdel, Noelia;
* Download [stable
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Download [development
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Presentazione #

Questo add-on è stato creato seguendo una richiesta di un membro della
mailing list dei componenti aggiuntivi di NVDA.

Fornisce una scorciatoia da tastiera, NVDA + F4, che permette di recuperare
e annunciare la lingua impostata per la tastiera corrente.

Se premuto due volte, annuncia la lingua di default del sistema.

Nella sua prima versione, questo modulo era stato proposto come una funzione
da aggiungere alla configurazione di NVDA; in seguito è stato realizzato
come componente aggiuntivo.

## Note ##

Se la combinazione di tasti NVDA+f4 è in conflitto con altri comandi, è
possibile modificarla nelle impostazioni tasti e gesti di immissione delle
preferenze di NVDA.

Lo script lo si trova nella categoria stato sistema.

## Compatibilità ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for version 20230426.0.0 and beyond##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Novità nella versione 19.02 ##

* Da ora, la numerazione delle versioni segue lo schema YY.MM (due cifre per
  l'anno, seguite da un punto e poi da due cifre per il mese);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Novità nella versione 1.1 ##

* Il componente è stato rinominato da getCurKeyboardLanguage in
  sayCurrentKeyboardLanguage;
* Aggiunta la licenza gpl al componente aggiuntivo;
* Aggiunto lo script getCurKeyboardLanguage alla categoria "Stato sistema";
* Sistemati alcuni errori nel codice.

## Novità nella versione 1.0 ##

* Versione iniziale.

[[!tag dev stable]]
