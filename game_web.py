from flask import Flask, render_template, request, redirect, url_for, session
import itertools
from game import generate_equation, operators

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "POST":
        op1 = request.form.get("operator1")
        op2 = request.form.get("operator2")
        if op1 not in operators or op2 not in operators:
            session["message"] = "Invalid input. Please enter valid operators."
        else:
            a, b, c, d, e = session["equation"]
            if eval(f"{a}{op1}{b}{op2}{c}{op3}{d}") == e:
                session["message"] = "Correct!"
                session["equation"] = generate_equation()
            else:
                session["message"] = f"Incorrect. Your guess: {op1} {op2}. Try again."
                session["attempts"] += 1
                if session["attempts"] >= 3:
                    for correct_op1, correct_op2 in itertools.product(operators, repeat=2):
                        if eval(f"{a}{correct_op1}{b}{correct_op2}{c}") == d:
                            session["message"] = f"The correct answer is: {correct_op1} {correct_op2}"
                            break
                    session["equation"] = generate_equation()
                    session["attempts"] = 0
    else:
        session["equation"] = generate_equation()
        session["attempts"] = 0
        session["message"] = ""

    return render_template("game.html", equation=session["equation"], message=session["message"])

if __name__ == "__main__":
    app.run(debug=True)
