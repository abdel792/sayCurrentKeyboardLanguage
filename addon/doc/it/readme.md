# sayCurrentKeyboardLanguage #

* Author(s): Abdel, Noelia.

# Presentazione #

Questo add-on è stato creato seguendo una richiesta di un membro della
mailing list dei componenti aggiuntivi di NVDA.

It provides a script without gesture, which allows to retrieve and give the
language of the current keyboard.

Se premuto due volte, annuncia la lingua di default del sistema.

Nella sua prima versione, questo modulo era stato proposto come una funzione
da aggiungere alla configurazione di NVDA; in seguito è stato realizzato
come componente aggiuntivo.

## Note ##

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

## Compatibilità ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20240326.0.0

* Updated compatibility for nvda-2024.1.;
* Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0 ##

* Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20230729.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.
* Removed the "NVDA + F4" gesture calling the script giving the keyboard
  language., to allow users to choose their preferred gesture.

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
