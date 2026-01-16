# Feature Request: Web-Based Investment Journal

**Status:** Open
**Assignee:** @Julia Tidalgo
**Context:** We want to move away from terminal scripts. We need a web page where I can write a journal entry, and the system automatically saves it with the current market data.

## 1. Setup
1.  Activate your venv.
2.  Run `pip install -r requirements.txt`.
3.  Run `python app.py` and open `http://127.0.0.1:5000` to make sure the site works.

## 2. The Mission
You need to build a new feature with two parts:

### Part A: The Frontend (HTML)
Create a new HTML file (e.g., `templates/journal.html`).
* It must have a `<form>` element.
* The form needs inputs for: `title` (text) and `content` (textarea).
* The form must submit data to the backend (Hint: `method="POST"`).

### Part B: The Backend (Flask)
Modify `app.py` to handle this new page.
1.  **The GET Route**: When I go to `/journal`, show me your new HTML form.
2.  **The POST Route**: When I submit the form:
    * Grab the data I typed.
    * Fetch the *current* market snapshot (use `fetch_market_snapshot()`).
    * Save everything to `journal_entries.json`.
    * **Bonus**: After saving, show a "Success" page that displays what I just wrote + the S&P 500 price at that moment.

## 3. Definition of Done
* [ ] I can go to `localhost:5000/journal` and see a form.
* [ ] When I click submit, a new entry appears in `journal_entries.json`.
* [ ] The JSON entry contains my text AND the market data.