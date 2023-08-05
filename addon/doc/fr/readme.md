# sayCurrentKeyboardLanguage #

* Auteurs : Abdel, Noelia;
* Télécharger [version
  stable](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Télécharger [version de
  développement](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Présentation #

Cette extension a été créée à la suite d'une demande d'un membre sur la
liste de diffusion nvda-addons.

Il fournit un script sans geste, NVDA + F4, qui permet de récupérer et de
donner la langue du clavier actuel.

Si vous appuyer deux fois sur la touche, vous donne la langue par défaut du
système.

À la première version de ce module, il a été proposé comme simple
globalPlugin afin d'être coller dans le répertoire de configuration de NVDA,
il a ensuite été transformé en extension.

## Notes ##

Pour définir un geste sur le script donnant la langue du clavier, suivez ces
étapes :

* Ouvrez le menu de NVDA, avec "NVDA + N" ;
* Allez au menu Préférences de NVDA ;
* Ensuite, allez au sous-menu "Gestes de commandes".
* Sélectionnez ensuite la catégorie "Entrée" et ouvrez-la avec la flèche
  droite.
* Allez à l'élément étiqueté "Annoncer la langue du clavier en cours
  d'utilisation. Un double appui annonce la langue du système." ;
* Une fois terminé, appuyez sur Alt + A pour ajouter un geste et tapez "NVDA
  + F4" ou un autre geste de votre choix ;
* Ceci fait, appuyez une fois sur la flèche haut, vous entendez "votre geste
  choisi, toutes les dispositions" ;
* Valider sur Entrée, puis Tab jusqu'à OK puis Entrée ;
* Votre geste choisi doit ensuite appeler le script donnant la langue du
  clavier.

## Compatibilité ##

* Cette extension est compatible avec les versions de NVDA allant de 2019.3
  et au-delà.

## Changements pour la  version 20230729.0.0 ##

* Appliqué les règles flake8 et mypy au code ;
* Modifiée la version minimale de NVDA prise en charge vers la 2019.3 pour
  prendre en charge les annotations introduites dans Python 3.
* Supprimé le geste "NVDA + F4" appelant le script donnant la langue du
  clavier, Pour permettre aux utilisateurs de choisir leur geste préféré.

## Changements pour la  version 20230426.0.0 et au-delà##

* Numéro de version modifiée, version minimale NVDA et lien de
  téléchargement en fonction des conventions / exigences de la store.

## Changements pour la version 19.02 ##

* Modification de la numérotation des versions en utilisant YY.MM (L'année
  en 2 chiffres, suivie d'un point, suivie du mois en 2 chiffres);
* Ajout de la compatibilité avec le nouveau format de gestion des versions
  des extensions, apparu depuis nvda 2019.1.

## Changements pour la version 1.1 ##

* L'extension a été renommée de getCurKeyboardLanguage en
  sayCurrentKeyboardLanguage;
* Ajout de la licence GPL à l'extension;
* Ajout du script getCurKeyboardLanguage dans la catégorie "État du
  système";
* Correction de quelques erreurs dans le code.

## Changements pour la version 1.0 ##

* Première version.

[[!tag dev stable]]
