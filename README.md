# Aegis

Un progetto personale in Python per sperimentare una chat da terminale con modelli linguistici locali tramite Ollama. Il codice separa interfaccia, gestione della conversazione, client HTTP e composizione dei prompt.

**Stato:** prototipo didattico in sviluppo. Il modello predefinito è `qwen3:4b`.

## Cosa fa

- Invia messaggi all'API di Ollama usando `urllib` e `json`, senza librerie Python esterne a runtime.
- Conserva in memoria la conversazione della sessione e la invia al modello a ogni richiesta.
- Compone un prompt di base con un profilo generalista (`normal`) oppure un profilo dedicato alla discussione di cybersecurity (`red-team`), con modulo opzionale `pentest`.
- Mostra stato e messaggi di log nel terminale.
- Gestisce gli errori di connessione intercettati come `URLError`, rimuovendo dalla cronologia la richiesta non riuscita.

I profili modificano soltanto le istruzioni testuali inviate al modello. Aegis non esegue comandi, non accede a file, non usa strumenti e non svolge attività di pentesting: l'interazione implementata è una chat.

## Avvio

Servono Python 3.12 o successivo, [Ollama installato](https://docs.ollama.com/quickstart) e in esecuzione, e il modello `qwen3:4b` disponibile localmente. La suite è stata verificata localmente con Python 3.13.0.

Una volta installato Ollama, scarica il modello:

```sh
ollama pull qwen3:4b
```

Se il servizio Ollama non è già attivo, avvialo in un altro terminale:

```sh
ollama serve
```

Dalla cartella principale del repository:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m src.main
```

Su Windows, attiva l'ambiente da PowerShell con `.venv\Scripts\Activate.ps1`.

Non è necessaria un'installazione di dipendenze Python per avviare la chat. Il primo download del modello richiede una connessione; con il modello già disponibile e la configurazione predefinita, le richieste di chat sono inviate al servizio locale.

Modalità disponibili:

```sh
python -m src.main normal
python -m src.main red-team
python -m src.main red-team pentest
```

Scrivi `exit` oppure `Exit` per chiudere la sessione; anche `Ctrl+C` interrompe la chat. La cronologia non viene salvata su disco.

## Configurazione

I valori sono definiti in [`src/config.py`](src/config.py):

| Impostazione | Valore predefinito |
| --- | --- |
| Modello | `qwen3:4b` |
| Host Ollama | `localhost` |
| Porta Ollama | `11434` |

Per usare un altro modello già installato, modifica `DEFAULT_MODEL`. La configurazione attuale non carica file `.env` né variabili d'ambiente.

## Struttura

```text
src/
  main.py                  # Interfaccia da terminale
  config.py                # Modello e indirizzo del servizio
  core/aegis.py            # Stato e cronologia della sessione
  llm/ollama_client.py      # Richieste HTTP all'API di Ollama
  prompts/                 # Prompt di base, profili e composizione
  utils/logger.py          # Log nel terminale
tests/                     # Test unitari con risposte simulate
.github/workflows/tests.yml
pytest.ini
requirements.txt
requirements-dev.txt
```

Il client include anche metodi per controllare la disponibilità del servizio, elencare i modelli e inviare una generazione singola. L'interfaccia interattiva usa il metodo `chat`.

## Test

Con l'ambiente virtuale attivo:

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

I 13 test esistenti verificano gli stati della sessione, l'aggiornamento della cronologia, la gestione della connessione non disponibile, i messaggi di log e il client Ollama attraverso mock. Non richiedono un servizio Ollama attivo e non misurano la qualità delle risposte del modello.

La configurazione GitHub Actions esegue la stessa suite con Python 3.12 su push e pull request. La presenza del file di configurazione non attesta un'esecuzione CI già completata.

## Limiti attuali

- Le chiamate HTTP sono sincrone, senza streaming e senza un timeout esplicito.
- La cronologia cresce per tutta la sessione: non sono implementati limiti, riassunti o gestione della finestra di contesto.
- Il parsing presume il formato atteso delle risposte Ollama; risposte JSON non valide o campi mancanti non sono gestiti in modo specifico.
- Gli errori della rete sono gestiti in modo essenziale; non sono previsti tentativi automatici o messaggi distinti per tutte le cause.
- I profili prompt non sono coperti da test dedicati; non è inclusa una verifica end-to-end con un modello reale.

## Licenza

La licenza di distribuzione è ancora da scegliere. Questa versione non include un file `LICENSE` e non concede una licenza open source.
