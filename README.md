# Aegis

Aegis è un laboratorio personale di ingegneria informatica nato con l'obiettivo di comprendere e costruire gradualmente un AI agent moderno.

Il valore principale del progetto non è soltanto il risultato finale, ma il processo di apprendimento: ogni componente viene sviluppato cercando prima di comprenderne il funzionamento, le motivazioni progettuali e i principi informatici su cui si basa.

L'obiettivo è approfondire progressivamente programmazione, architettura software, sistemi LLM, testing e cybersecurity, partendo dalle basi prima di affrontare sistemi più complessi.

> Fino a superare i limiti del possibile...

---

## Stato del progetto

**Aegis v1.0.0**

La prima versione stabile implementa una chat da terminale collegata a un modello linguistico locale tramite Ollama, con architettura modulare, memoria conversazionale di sessione, profili differenti e test automatici.

Il progetto utilizza attualmente:

- Python
- Ollama
- Qwen3 4B
- pytest

---

## Funzionalità

### Chat locale

Aegis comunica con Ollama tramite API HTTP locali.

La conversazione viene mantenuta durante la sessione attraverso una cronologia composta dai ruoli:

- `system`
- `user`
- `assistant`

La memoria è attualmente mantenuta solamente in RAM e viene persa alla chiusura del programma.

### Modalità Normal

Profilo generalista dedicato principalmente a:

- programmazione
- informatica
- STEM
- studio
- debugging
- problem solving

Avvio:

```bash
python3 -m src.main
```

oppure:

```bash
python3 -m src.main normal
```

### Modalità RED

Profilo dedicato allo studio della cybersecurity in ambienti autorizzati, laboratori, CTF e sistemi personali.

Avvio:

```bash
python3 -m src.main red-team
```

È inoltre disponibile il modulo Pentest:

```bash
python3 -m src.main red-team pentest
```

Il modulo segue un approccio evidence-driven basato su enumerazione, formulazione di ipotesi e validazione progressiva.

---

## Architettura dei prompt

Aegis utilizza un sistema modulare:

```text
AEGIS_CORE
│
├── NORMAL_PROFILE
│
└── RED_CORE
     │
     └── PENTEST_MODULE
```

`AEGIS_CORE` contiene i principi condivisi dalle diverse modalità, mentre i profili e i moduli specializzati vengono composti dinamicamente tramite il prompt builder.

---

## Struttura del progetto

```text
Aegis/
├── src/
│   ├── core/
│   ├── prompts/
│   ├── config.py
│   └── main.py
├── tests/
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Installazione

Creare e attivare un ambiente virtuale:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installare le dipendenze:

```bash
pip install -r requirements.txt
```

Installare Ollama e scaricare il modello:

```bash
ollama pull qwen3:4b
```

Ollama deve essere in esecuzione prima di avviare Aegis.

---

## Testing

La suite automatica può essere eseguita con:

```bash
python3 -m pytest
```

Stato della v1.0.0:

```text
13 passed
```

I test coprono il core di Aegis, il logger e il client Ollama.

---

## Gestione degli errori

Aegis gestisce alcuni casi comuni senza terminare con traceback inutili, tra cui:

- Ollama non disponibile
- interruzione tramite `Ctrl+C`
- modulo RED non valido

---

## Limiti attuali

La versione 1.0.0 non implementa ancora:

- memoria persistente
- streaming delle risposte
- accesso diretto ai file
- browser
- tool execution
- RAG
- GUI

Queste funzionalità possono essere esplorate in versioni future.

---

## Obiettivo

Aegis non nasce come sostituto di assistenti AI commerciali.

È principalmente un progetto personale di studio e sperimentazione utilizzato per approfondire concretamente software engineering, API locali, architetture LLM, testing, gestione dello stato, progettazione modulare e cybersecurity.

La v1.0.0 rappresenta la conclusione della prima fase del progetto.
