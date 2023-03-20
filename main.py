import flask
from flask import Flask, render_template, url_for, request

def rechner():
    x1 = int(input("Dein erste Zahl:"))
    operator = input("Rechenoperator:" )
    x2 = int(input("Deine zweite Zahl:"))
    if operator == "geteilt":
        print(x1/x2)
    if operator == "mal":
        print(x1*x2)
    if operator == "minus":
        print(x1-x2)
    if operator == "plus":
        print(x1+x2)


app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])

def index():
    return render_template("index.html")


@app.route("/result",methods = ['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    first_digit = float(output["fdigit"])
    second_digit = float(output["sdigit"])
    ergebnis = first_digit*second_digit
    return render_template("index.html", ergebnis=ergebnis)


if __name__ == '__main__':
   app.run(port=5001, debug=True)