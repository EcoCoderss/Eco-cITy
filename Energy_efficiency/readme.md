
---

## Dettagli sulla Struttura

### 1. **Cartella `data/`**
- Destinata a contenere i dataset utilizzati dal microservizio.
- Attualmente vuota. Scarica il dataset dal link fornito (vedi sezione **Dataset**) e posizionalo qui.

### 2. **Cartella `agents/`**
- Contiene la logica per orchestrare le chiamate al modello AI.
- `energy_optimizer_agent.py`: Chiama il servizio Watsonx.ai con i dati forniti e restituisce le previsioni/ottimizzazioni.

### 3. **Cartella `models/`**
- Definisce i modelli per rappresentare input e output.
- `energy_analysis.py`: Struttura dei dati utilizzati per comunicare con l'AI.

### 4. **Cartella `routers/`**
- Gestisce le rotte API per l'interazione con il microservizio.
- `energy_router.py`: Fornisce endpoint REST per ricevere dati e restituire risultati.

### 5. **Cartella `services/`**
- Implementa la logica di integrazione con servizi esterni.
- `watsonx_service.py`: Effettua chiamate a **IBM Watsonx.ai** e gestisce i dataset con **IBM Watsonx.data**.
  - **Perché `watsonx_service.py`?**
    - Centralizza la logica di comunicazione con Watsonx.ai.
    - Facilita la gestione di dataset (caricamento, trasformazione, validazione).
    - Garantisce modularità e riutilizzabilità del codice.

### 6. **Cartella `tests/`**
- Contiene test per assicurare che il microservizio funzioni correttamente.
- `test_energy_analysis.py`: Verifica la validità dei dati e la comunicazione con Watsonx.ai.

### 7. **`Dockerfile`**
- Definisce l'immagine Docker per eseguire il microservizio in un ambiente isolato.

### 8. **`requirements.txt`**
- Elenca le dipendenze necessarie per il progetto.

---

## Dataset

### **Nome**: NYC Energy Consumption Survey
- **Descrizione**: Dataset che contiene informazioni sui consumi energetici degli edifici di New York.
- **Utilizzo**: Fornire dati al modello AI per l'analisi e l'ottimizzazione.
- **Link per il download**: [NYC Energy Dataset](https://www.kaggle.com/datasets/claytonmiller/new-york-city-buildings-energy-consumption-survey).
- **Posizionamento**: Scarica e salva il file `.csv` nella cartella `data/`.

---

## Come iniziare

### 1. **Setup ambiente**
- Installa le dipendenze:
  ```bash
  pip install -r requirements.txt
