# sayCurrentKeyboardLanguage

* Autor(zy): Abdel, Noelia.

# Prezentacja #

Ten dodatek został stworzony na prośbę jednego z członków listy dyskusyjnej nvda-addons.

Dostarcza on skrypt bez przypisanego gestu, który pozwala pobrać i oznajmić język bieżącego układu klawiatury.

Naciśnięty dwukrotnie, podaje domyślny język systemu.

W pierwszej wersji tego modułu był on proponowany jako prosty globalPlugin do wklejenia do katalogu konfiguracyjnego NVDA, a następnie został przekształcony w dodatek.

## Uwagi ##

Aby przypisać gest do skryptu podającego język klawiatury, wykonaj następujące kroki:

* Otwórz menu NVDA za pomocą "NVDA + N";
* Przejdź do menu Preferencje NVDA;
* Następnie przejdź do podmenu "Zdarzenia wejściowe".
* Następnie wybierz kategorię "Wprowadzanie danych" i otwórz ją prawą strzałką.
* Przejdź do elementu o nazwie "Podaje język używanej klawiatury, naciśnięty dwukrotnie, podaje domyślny język systemu";
* Po zakończeniu naciśnij Alt + A, aby dodać gest, i wpisz "NVDA + F4" lub inny wybrany gest;
* Po wykonaniu tej czynności naciśnij raz strzałkę w górę, usłyszysz "twój wybrany gest, wszystkie układy";
* Zatwierdź klawiszem Enter, a następnie przejdź tabulatorem do OK i naciśnij Enter;
* Wybrany gest powinien teraz wywoływać skrypt podający język klawiatury.

## Kompatybilność ##

* Ten dodatek jest kompatybilny z wersjami NVDA od 2019.3 i nowszymi.

## Zmiany w 20240326.0.0

* Zaktualizowano kompatybilność dla nvda-2024.1;
* Usunięto link do pobierania z pliku readme, link do pobierania przyszłych aktualizacji będzie teraz dostępny wyłącznie w sklepie z dodatkami.

## Zmiany w 20231229.0.0 ##

* Dodano wstecznie kompatybilną implementację obsługującą tryb mowy na żądanie, który wkrótce będzie dostępny w nvda-2024.1.

## Zmiany w 20230729.0.0 ##

* Zastosowano reguły flake8 i mypy do kodu;
* Zmieniono minimalną obsługiwaną wersję NVDA na 2019.3, aby obsługiwać adnotacje wprowadzone w Pythonie 3.
* Usunięto gest "NVDA + F4" wywołujący skrypt podający język klawiatury, aby umożliwić użytkownikom wybór preferowanego gestu.

## Zmiany w 20230607.0.0 ##

* Dodano następujące przepływy pracy (workflows):
 * auto-update-translations - do automatycznej aktualizacji tłumaczeń z systemu tłumaczeń NVDA.
 * release-on-tag..yaml: do budowania i publikowania dodatku, gdy tylko pojawi się nowy tag;
 * manual-release.yaml: do ręcznego budowania i wydawania nowych wersji dodatku.
* Zaktualizowano tłumaczenia.

## Zmiany w wersji 20230426.0.0 i nowszych ##

* • Zmieniono numer wersji, minimalną wersję NVDA i link do pobierania zgodnie z konwencjami/wymogami sklepu.

## Zmiany w wersji 19.02 ##

* Zmieniono numerację wersji przy użyciu formatu RR.MM (rok w postaci 2 cyfr, po którym następuje kropka, a następnie miesiąc w postaci 2 cyfr);
* Dodano kompatybilność z nowym formatem numeracji wersji dodatków, który pojawił się od nvda 2019.1.

## Zmiany w wersji 1.1 ##

* Nazwa dodatku została zmieniona z getCurKeyboardLanguage na sayCurrentKeyboardLanguage;
* Dodano licencję GPL do dodatku;
* Dodano skrypt getCurKeyboardLanguage do kategorii "Status systemu";
* Naprawiono kilka błędów w kodzie.

## Zmiany w wersji 1.0 ##

* Wersja początkowa.
