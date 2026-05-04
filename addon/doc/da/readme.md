# sayCurrentKeyboardLanguage

- Author(s): Abdel, Noelia.

# Præsentation

Denne tilføjelse blev oprettet efter en anmodning fra et medlem på
mailinglisten for nvda-addons.

It provides a script without gesture, which allows to retrieve and give the
language of the current keyboard.

Hvis du trykker to gange, angiver systemets standardsprog.

At the first version of this module, it had been proposed as simple globalPlugin to paste in the configuration directory of NVDA, it was then transformed into addon.

## Noter

To set a gesture to the script giving the keyboard language, follow these
steps:

- Open the NVDA's menu, with "NVDA + N";
- Go to NVDA's preferences menu;
- Then go to the submenu "Input gestures".
- Then select the category "Input", and open it with right arrow.
- Go to the item labeled "Gives the language of the keyboard in use, if
  pressed twice, give the default language of the system";
- Once done, press Alt + A to add a gesture, and type "NVDA + F4" or another
  gesture of your choice;
- This done, press the up arrow once, you hear "your chosen gesture, all
  layout";
- Validate on enter, then tab to OK then enter;
- Your chosen gesture should then call the script giving keyboard language.

## Kompatibilitet

- This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20240326.0.0

- Updated compatibility for nvda-2024.1.;
- Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0

- Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20230729.0.0

- Applied the flake8 and mypy rules to the code;
- Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.
- Removed the "NVDA + F4" gesture calling the script giving the keyboard
  language., to allow users to choose their preferred gesture.

## Changes for version 20230426.0.0 and beyond#\#

- Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.
- auto-update-translations - to automatically update translations from NVDA's translation system.
- release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
- manual-release.yaml: to build and release new versions of the add-on manually.
- Updated translations.

## Ændringer for version 19.02

- Ændret versionsnummerering til åå.MM (År i 2 cifre efterfulgt af et
  punktum, efterfulgt af måneden i 2 cifre);

## Ændringer for version 1.1

- Tilføjelsen er blevet omdøbt fra getCurKeyboardLanguage til
  sayCurrentKeyboardLanguage;
- Tilføjet GPL-licensen til tilføjelsen;

## Ændringer for version 1.0

- Første version.
- Added the GPL license to the addon;
- Added the script getCurKeyboardLanguage to the "System status" category;
- Fixed some errors in the code.

## Changes for version 1.0

- Initial version.
