# Dizer o Idioma Atual do Teclado (sayCurrentKeyboardLanguage) #

* Autor(es): Abdel, Noelia;
* Download [stable
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Download [development
  version](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Apresentação #

Este complemento foi criado após uma solicitação de um membro da lista de
discussão nvda-addons.

Provê um atalho de teclado, NVDA+F4, que permite recuperar e fornecer o
idioma do teclado atual.

Se pressionado duas vezes, fornece o idioma padrão do sistema.

Na primeira versão deste módulo, foi proposto como simples plug-in global
(globalPlugin) para colar no diretório de configuração do NVDA, depois foi
transformado em complemento (add-on).

## Notas ##

Se o atalho de teclado NVDA+F4 entrar em conflito com outro comando, você
poderá alterá-lo acessando o menu Preferências do NVDA, no submenu "Definir
comandos".

Você encontrará o script na categoria "Status do sistema".

## Compatibilidade ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

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
