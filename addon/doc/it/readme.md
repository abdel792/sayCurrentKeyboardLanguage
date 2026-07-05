# sayCurrentKeyboardLanguage

* Autore(i): Abdel, Noelia.

# Presentazione #

Questo componente aggiuntivo è stato creato su richiesta di un membro della mailing list nvda-addons.

Fornisce uno script senza tasto di scelta rapida, che consente di recuperare e pronunciare la lingua della tastiera corrente.

Se premuto due volte, fornisce la lingua predefinita del sistema.

Alla prima versione di questo modulo, era stato proposto come semplice globalPlugin da incollare nella directory di configurazione di NVDA, successivamente è stato trasformato in componente aggiuntivo.

## Note ##

Per assegnare un tasto di scelta rapida allo script che fornisce la lingua della tastiera, segui questi passaggi:

* Apri il menu di NVDA con "NVDA + N";
* Vai al menu delle preferenze di NVDA;
* Quindi vai al sottomenu "Gesti di immissione".
* Seleziona quindi la categoria "Immissione" e aprila con la freccia destra.
* Vai alla voce etichettata "Fornisce la lingua della tastiera in uso, se premuto due volte, fornisce la lingua predefinita del sistema";
* Una volta fatto, premi Alt + A per aggiungere un gesto e digita "NVDA + F4" o un altro gesto a tua scelta;
* Fatto questo, premi la freccia su una volta, sentirai "il gesto scelto, tutti i layout";
* Conferma con Invio, quindi usa il Tab per andare su OK e premi Invio;
* Il gesto scelto dovrebbe quindi chiamare lo script che fornisce la lingua della tastiera.

## Compatibilità ##

* Questo componente aggiuntivo è compatibile con le versioni di NVDA a partire dalla 2019.3 e successive.

## Modifiche per 20240326.0.0

* Compatibilità aggiornata per nvda-2024.1;
* Eliminato il link di download dal readme, il link di download per i futuri aggiornamenti sarà ora disponibile solo dal negozio dei componenti aggiuntivi.

## Modifiche per 20231229.0.0 ##

* Aggiunta un'implementazione retrocompatibile per supportare la modalità di sintesi vocale su richiesta, che sarà presto disponibile con nvda-2024.1.

## Modifiche per 20230729.0.0 ##

* Applicate le regole flake8 e mypy al codice;
* Modificata la versione minima di NVDA supportata alla 2019.3 per supportare le annotazioni introdotte in Python 3.
* Rimosso il gesto "NVDA + F4" che chiamava lo script che fornisce la lingua della tastiera, per consentire agli utenti di scegliere il proprio gesto preferito.

## Modifiche per 20230607.0.0 ##

* Aggiunti i seguenti flussi di lavoro:
 * auto-update-translations - per aggiornare automaticamente le traduzioni dal sistema di traduzione di NVDA.
 * release-on-tag..yaml: per compilare e pubblicare il componente aggiuntivo non appena viene inviato un nuovo tag;
 * manual-release.yaml: per compilare e rilasciare manualmente nuove versioni del componente aggiuntivo.
* Traduzioni aggiornate.

## Modifiche per la versione 20230426.0.0 e successive ##

* • Modificato il numero di versione, la versione minima di NVDA e il link di download in base alle convenzioni/requisiti del negozio.

## Modifiche per la versione 19.02 ##

* Modificata la numerazione delle versioni utilizzando AA.MM (L'anno in 2 cifre, seguito da un punto, seguito dal mese in 2 cifre);
* Aggiunta la compatibilità con il nuovo formato di numerazione delle versioni dei componenti aggiuntivi, apparso a partire da nvda 2019.1.

## Modifiche per la versione 1.1 ##

* Il componente aggiuntivo è stato rinominato da getCurKeyboardLanguage a sayCurrentKeyboardLanguage;
* Aggiunta la licenza GPL al componente aggiuntivo;
* Aggiunto lo script getCurKeyboardLanguage alla categoria "Stato del sistema";
* Corretti alcuni errori nel codice.

## Modifiche per la versione 1.0 ##

* Versione iniziale.
