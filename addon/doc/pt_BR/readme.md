# Dizer o Idioma Atual do Teclado (sayCurrentKeyboardLanguage) #

* Autor(es): Abdel, Noelia;
* Download [stable
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Download [development
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Apresentação #

Este complemento foi criado após uma solicitação de um membro da lista de
discussão nvda-addons.

It provides a script without gesture, which allows to retrieve and give the
language of the current keyboard.

Se pressionado duas vezes, fornece o idioma padrão do sistema.

Na primeira versão deste módulo, foi proposto como simples plug-in global
(globalPlugin) para colar no diretório de configuração do NVDA, depois foi
transformado em complemento (add-on).

## Notas ##

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

## Compatibilidade ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230729.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.
* Removed the "NVDA + F4" gesture calling the script giving the keyboard
  language., to allow users to choose their preferred gesture.

## Changes for version 20230426.0.0 and beyond##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Mudanças na versão 19.02 ##

* Numeração de versão alterada usando AA.MM (o ano em 2 dígitos, seguido de
  um ponto, seguido do mês em 2 dígitos);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Mudanças na versão 1.1 ##

* O complemento foi renomeado de getCurKeyboardLanguage (Obtenha o Idioma
  Atual do Teclado) para sayCurrentKeyboardLanguage (Dizer o Idioma Atual do
  Teclado);
* Adicionada a licença GPL ao complemento;
* Adicionado o script getCurKeyboardLanguage à categoria "Status do
  sistema";
* Corrigido alguns erros no código.

## Mudanças na versão 1.0 ##

* Versão inicial.

[[!tag dev stable]]
