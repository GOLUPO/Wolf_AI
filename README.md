# Wolf_AI

Wolf_AI è un'applicazione che permette agli utenti di interagire con un assistente AI, salvare e gestire chat, e personalizzare il proprio profilo utente con immagini e credenziali aggiornabili. L'applicazione utilizza modelli GPT-3.5 e GPT-4 optimized di OpenAI per generare risposte e nomi delle chat.

## Funzionalità

- **Registrazione e Login:** Gli utenti possono registrarsi e accedere utilizzando un nome utente e una password.
- **Dashboard:** Gli utenti possono visualizzare e modificare le proprie credenziali, aggiornare l'immagine del profilo e visualizzare le chat salvate.
- **Chat con AI:** Gli utenti possono creare nuove chat, inviare messaggi all'assistente AI e ricevere risposte generate dai modelli GPT-3.5 e GPT-4 optimized di OpenAI.
- **Salvataggio delle Chat:** Le chat vengono salvate e possono essere ricaricate in un secondo momento.
- **Generazione del Nome della Chat:** Il nome della chat viene generato automaticamente dopo il secondo messaggio dell'utente utilizzando il modello GPT-4 optimized mini.
- **Gestione delle Immagini di Profilo:** Gli utenti possono caricare e aggiornare la propria immagine del profilo.

## Requisiti

- Python 3.6 o superiore
- Flask
- Werkzeug
- OpenAI API key

## Installazione

1. **Clona il repository:**

    ```bash
    git clone https://github.com/GOLUPO/Wolf_AI.git
    cd Wolf_AI
    ```

2. **Crea e attiva un ambiente virtuale:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Su Windows usa `venv\Scripts\activate`
    ```

3. **Installa le dipendenze:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configura la chiave API di OpenAI:**

    Crea un file `.env` nella directory principale del progetto e aggiungi la tua chiave API di OpenAI:

    ```bash
    OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
    ```

5. **Crea le directory necessarie:**

    ```bash
    mkdir chats
    mkdir profile_pics
    ```

6. **Esegui l'applicazione:**

    ```bash
    flask run
    ```

## Utilizzo

1. **Registrazione:**
   Apri il browser e vai a `http://127.0.0.1:5000/register`. Inserisci un nome utente e una password per creare un nuovo account.

2. **Login:**
   Dopo la registrazione, vai a `http://127.0.0.1:5000/login` per accedere con il tuo nome utente e la tua password.

3. **Dashboard:**
   Dopo aver effettuato l'accesso, sarai reindirizzato alla homepage. Clicca su "Account" per accedere alla dashboard dove potrai aggiornare le tue credenziali, caricare un'immagine di profilo e visualizzare le tue chat salvate.

4. **Creazione di una Nuova Chat:**
   Clicca su "Nuova Chat" nella sidebar per creare una nuova chat. Inserisci un messaggio nel campo di input e premi "Invia". L'assistente AI risponderà e la chat verrà salvata automaticamente.

5. **Generazione del Nome della Chat:**
   Dopo aver inviato il secondo messaggio, il nome della chat verrà generato automaticamente utilizzando il modello GPT-4 optimized mini.

6. **Aggiornamento dell'Immagine del Profilo:**
   Nella dashboard, carica una nuova immagine di profilo e clicca su "Update" per salvare le modifiche.

## Struttura del Progetto

- `app.py`: File principale dell'applicazione Flask che contiene le rotte e la logica del server.
- `templates/`: Directory che contiene i file HTML per le diverse pagine (index, login, register, dashboard).
- `static/`: Directory che contiene i file CSS e le risorse statiche.
- `chats/`: Directory dove vengono salvate le chat.
- `profile_pics/`: Directory dove vengono salvate le immagini di profilo degli utenti.
- `users.json`: File JSON che contiene le informazioni sugli utenti registrati.

## Contributi

I contributi sono benvenuti! Sentiti libero di aprire issue o pull request per migliorare l'applicazione.
