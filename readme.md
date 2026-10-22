# Finance Tracker

A small personal finance tracker built as a learning project with Python, Flask, and SQLite.

## Features

- Add a transaction with a description, amount, category, and date
- Save transactions in a local SQLite database
- View saved transactions in a table

## Built With

- Python
- Flask
- SQLite
- HTML
- CSS

## Run Locally

These instructions assume Ubuntu on WSL.

1. Clone the repository:

   ```bash
   git clone https://github.com/sn2368/finance-tracker
   cd finance-tracker
   ```

2. Install the required packages if they aren’t already installed:

   ```bash
   sudo apt update
   sudo apt install python3-flask sqlite3
   ```

3. Create the local database and table:

   ```bash
   sqlite3 finance.db < schema.sql
   ```

4. Start the Flask app:

   ```bash
   python3 app.py
   ```

5. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Data and Privacy

The app stores transactions in a local SQLite database file named `finance.db`. That generated file should stay on your computer and should not be committed to GitHub. The app is a learning project and is not intended for sensitive financial data.

## Project Status

This project is a work in progress.
