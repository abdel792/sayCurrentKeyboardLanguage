# sayCurrentKeyboardLanguage #

* Auteurs : Abdel, Noelia;
* Télécharger [version stable][1];
* Télécharger [version de développement][2].

# Présentation #

Ce module complémentaire a été créé à la suite d'une demande d'un membre sur
la liste de diffusion nvda-addons.

Il fournit un raccourci clavier, NVDA + F4, qui permet de récupérer et de
donner la langue du clavier actuel.

Si vous appuyer deux fois sur la touche, vous donne la langue par défaut du
système.

À la première version de ce module, il a été proposé comme simple
globalPlugin afin d'être coller dans le répertoire de configuration de NVDA,
il a ensuite été transformé en module complémentaire.

## Notes ##

Si le raccourci du clavier NVDA + F4 entre en conflit avec une autre
commande, vous pouvez le modifier en allant dans le menu Préférences de
NVDA, dans le sous-menu "Gestes de commandes".

Vous trouverez ensuite le script dans la catégorie "État du système".

## Compatibilité ##

* Ce module complémentaire est compatible avec les versions de NVDA allant
  de 2014.3 à 2019.1.

## Changements pour la version 19.02 ##

* Modification de la numérotation des versions en utilisant YY.MM (L'année
  en 2 chiffres, suivie d'un point, suivie du mois en 2 chiffres);
* Ajout de la compatibilité avec le nouveau format de gestion des versions
  du module complémentaire, apparu depuis la nvda 2019.1.

## Changements pour la version 1.1 ##

* Le module complémentaire a été renommé de getCurKeyboardLanguage en
  sayCurrentKeyboardLanguage;
* Ajout de la licence GPL au module complémentaire;
* Ajout du script getCurKeyboardLanguage dans la catégorie "État du
  système";
* Correction de quelques erreurs dans le code.

## Changements pour la version 1.0 ##

* Première version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ckbl

[2]: https://addons.nvda-project.org/files/get.php?file=ckbl-dev
