from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    transaction = None
    error = None

    if request.method == "POST":
        description = request.form.get("description", "").strip()
        category = request.form.get("category", "").strip()
        date = request.form.get("date", "").strip()
        amount_text = request.form.get("amount", "").strip()

        if not description or not category or not date:
            error = "Please fill in all the fields."

        try:
            amount = float(amount_text)
            if amount <= 0:
                error = "Enter an amount greater than zero."
        except ValueError:
            error = "Enter a valid amount."

        if not error:
            connection = sqlite3.connect("finance.db")
            try:
                connection.execute(
                    """
                    INSERT INTO transactions
                        (description, amount, category, transaction_date)
                    VALUES (?, ?, ?, ?)
                    """,
                    (description, amount, category, date),
                )
                connection.commit()
            finally:
                connection.close()

            transaction = {
                "description": description,
                "amount": amount,
                "category": category,
                "date": date,
            }
    
    connection = sqlite3.connect("finance.db")
    transactions = connection.execute("SELECT description, amount, category, transaction_date ""FROM transactions ORDER BY transaction_date DESC, id DESC").fetchall()
    connection.close()
    return render_template(
        "index.html",
        transaction=transaction,
        error=error, transactions=transactions,
    )


if __name__ == "__main__":
    app.run(debug=True)
