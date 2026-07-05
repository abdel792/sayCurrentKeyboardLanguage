# sayCurrentKeyboardLanguage

* Auteur(s) : Abdel, Noelia.

# Présentation #

Cette extension a été créée à la demande d'un membre de la liste de diffusion nvda-addons.

Elle fournit un script sans geste, qui permet de récupérer et de donner la langue du clavier actuel.

Si pressé deux fois, donne la langue par défaut du système.

À la première version de ce module, il avait été proposé comme simple globalPlugin à coller dans le répertoire de configuration de NVDA, il a ensuite été transformé en extension.

## Notes ##

Pour attribuer un geste au script donnant la langue du clavier, suivez ces étapes :

* Ouvrez le menu de NVDA, avec "NVDA + N" ;
* Allez dans le menu des préférences de NVDA ;
* Allez ensuite dans le sous-menu "Gestes d'entrée".
* Sélectionnez ensuite la catégorie "Saisie", et ouvrez-la avec la flèche droite.
* Allez sur l'élément intitulé "Donne la langue du clavier en cours d'utilisation, si pressé deux fois, donne la langue par défaut du système" ;
* Une fois cela fait, appuyez sur Alt + A pour ajouter un geste, et tapez "NVDA + F4" ou un autre geste de votre choix ;
* Cela fait, appuyez une fois sur la flèche haut, vous entendez "votre geste choisi, toutes les dispositions" ;
* Validez par Entrée, puis tabulez jusqu'à OK puis Entrée ;
* Le geste de votre choix devrait alors appeler le script donnant la langue du clavier.

## Compatibilité ##

* Cette extension est compatible avec les versions de NVDA allant de 2019.3 et supérieures.

## Changements pour 20240326.0.0

* Compatibilité mise à jour pour nvda-2024.1 ;
* Suppression du lien de téléchargement du readme, le lien de téléchargement pour les futures mises à jour sera désormais uniquement disponible depuis la boutique d'extensions.

## Changements pour 20231229.0.0 ##

* Ajout d'une implémentation rétrocompatible pour prendre en charge le mode de parole à la demande, qui sera bientôt disponible avec nvda-2024.1.

## Changements pour 20230729.0.0 ##

* Appliqué les règles flake8 et mypy au code ;
* Changé la version minimale de NVDA prise en charge à 2019.3 pour supporter les annotations introduites dans Python 3.
* Supprimé le geste "NVDA + F4" appelant le script donnant la langue du clavier, pour permettre aux utilisateurs de choisir leur geste préféré.

## Changements pour 20230607.0.0 ##

* Ajout des flux de travail suivants :
 * auto-update-translations - pour mettre à jour automatiquement les traductions depuis le système de traduction de NVDA.
 * release-on-tag..yaml : pour compiler et publier l'extension dès qu'un nouveau tag est poussé ;
 * manual-release.yaml : pour compiler et publier de nouvelles versions de l'extension manuellement.
* Traductions mises à jour.

## Changements pour la version 20230426.0.0 et supérieures ##

* • Changé le numéro de version, la version minimale de NVDA et le lien de téléchargement selon les conventions/exigences de la boutique.

## Changements pour la version 19.02 ##

* Changé la numérotation des versions en utilisant AA.MM (L'année en 2 chiffres, suivie d'un point, suivie du mois en 2 chiffres) ;
* Ajout de la compatibilité avec le nouveau format de numérotation des versions de l'extension, apparu depuis nvda 2019.1.

## Changements pour la version 1.1 ##

* L'extension a été renommée de getCurKeyboardLanguage à sayCurrentKeyboardLanguage ;
* Ajout de la licence GPL à l'extension ;
* Ajout du script getCurKeyboardLanguage à la catégorie "État du système" ;
* Correction de quelques erreurs dans le code.

## Changements pour la version 1.0 ##

* Version initiale.
