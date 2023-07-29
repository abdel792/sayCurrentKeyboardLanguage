# sayCurrentKeyboardLanguage

* Author(s): Abdel, Noelia;
* Download [stable version][1];
* Download [development version][2].

# Presentation #

This addon was created following a request from a member on the nvda-addons mailing list.

It provides a script without gesture, which allows to retrieve and give the language of the current keyboard.

If pressed twice, gives the default language of the system.

At the first version of this module, it had been proposed as simple globalPlugin to paste in the configuration directory of NVDA, it was then transformed into addon.

## Notes ##

To set a gesture to the script giving the keyboard language, follow these steps:

* Open the NVDA's menu, with "NVDA + N";
* Go to NVDA's preferences menu;
* Then go to the submenu "Input gestures".
* Then select the category "Input", and open it with right arrow.
* Go to the item labeled "Gives the language of the keyboard in use, if pressed twice, give the default language of the system";
* Once done, press Alt + A to add a gesture, and type "NVDA + F4" or another gesture of your choice;
* This done, press the up arrow once, you hear "your chosen gesture, all layout";
* Validate on enter, then tab to OK then enter;
* Your chosen gesture should then call the script giving keyboard language.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3 and beyond.

## Changes for 20230729.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support annotations introduced in Python 3.
* Removed the "NVDA + F4" gesture calling the script giving the keyboard language., to allow users to choose their preferred gesture.

## Changes for 20230607.0.0 ##

* Added the following workflows:
 * auto-update-translations - to automatically update translations from NVDA's translation system.
 * release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
 * manual-release.yaml: to build and release new versions of the add-on manually.
* Updated translations.

## Changes for version 20230426.0.0 and beyond ##

* • Changed version number, minimum NVDA version and download link according to store conventions/requirements.

## Changes for version 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared since nvda 2019.1.

## Changes for version 1.1 ##

* The addon has been renamed from getCurKeyboardLanguage to sayCurrentKeyboardLanguage;
* Added the GPL license to the addon;
* Added the script getCurKeyboardLanguage to the "System status" category;
* Fixed some errors in the code.

## Changes for version 1.0 ##

* Initial version.

[1]: https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage

[2]: https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage
