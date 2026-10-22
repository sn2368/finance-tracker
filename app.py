from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    transaction = None
    error = None

    if request.method == "POST":
        description = request.form.get("description", "").strip()
        category = request.form.get("category", "").strip()
        date = request.form.get("date", "").strip()

        try:
            amount = float(request.form.get("amount", ""))
            if amount <= 0:
                raise ValueError
        except ValueError:
            error = "Enter an amount greater than zero."

        if not description or not category or not date:
            error = "Please fill in all the fields."

        if not error:
            transaction = {
                "description": description,
                "amount": amount,
                "category": category,
                "date": date,
            }

    return render_template("index.html", transaction=transaction, error=error)


if __name__ == "__main__":
    app.run(debug=True)
