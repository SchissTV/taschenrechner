import flask
from flask import Flask, render_template, url_for, request
import math_own
import sqlite3

# Datenbank-Integration
conn = sqlite3.connect('history_calc.db')
cursor = conn.cursor()



table_name = 'history'
cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
result = cursor.fetchone()

if result:
    print("Datenbank existiert bereits. fahre fort")
else:
    cursor.execute('CREATE TABLE history(number INTEGER, rechnung TEXT, ergebnis TEXT)')
    print("Database table wurde erstellt")
cursor.close()
conn.close()


conn = sqlite3.connect('history_calc.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM history WHERE number="1"')
no_entry_yet = cursor.fetchall()
print("no_entry_yet", no_entry_yet)
if no_entry_yet[0] is None:
    cursor.execute('INSERT INTO history VALUES (1, "2 * 2", "25")')
    conn.commit()

cursor.close()
conn.close()

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])

def index():
    return render_template("index.html")


@app.route("/result",methods = ['POST', 'GET'])
def result():
    # sqlite connection
    conn = sqlite3.connect('history_calc.db')
    cursor = conn.cursor()
    
    output = request.form.to_dict()
    print(output)
    digit = str(output["digit"])
    ergebnis = math_own.main(digit)
    print(digit)
    
    # getting max previous number
    cursor.execute('SELECT MAX(number) FROM history')
    get_max_number = cursor.fetchall()
    print(get_max_number[0])
    max_number = int(sum(get_max_number[0])) if get_max_number[0] is not None else 0
    
    # verlauf erstellen
    cursor.execute('INSERT INTO history VALUES (?, ?, ?)', (int(max_number+1), digit, ergebnis))
    conn.commit()
    cursor.execute('SELECT * FROM history')
    ausgabe = cursor.fetchone()
    print(ausgabe)

    cursor.close()
    conn.close()
    # ausgabe
    return render_template("index.html", value=ergebnis)

if __name__ == '__main__':
    app.run(port=5001, debug=True)

def get_max_number():
    cursor.execute('SELECT MAX(number) FROM history')
    return cursor.fetchone()

max_number = int(get_max_number()[0]) if get_max_number() and get_max_number()[0] is not None else 0

