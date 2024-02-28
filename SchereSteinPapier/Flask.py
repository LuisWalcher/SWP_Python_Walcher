import sqlite3

from flask import Flask, request, app
import main



app = Flask(__name__)

def get_connection():
    return sqlite3.connect("SchereSteinPapier.db")


@app.route('/',methods=['POST'])
def handle_json():
    if request.is_json:
        data = request.json
        print(data)
        save_data(data)
        print(data.get("Results").get("Schere"))
        return data
    else:
        return "Anfrage enthält keine Json-Daten!"

def save_data(data):
    connection = get_connection()
    print(connection.total_changes)
    cursor = connection.cursor()
    cursor.execute("Create table if not exists Gamedata (AnzSchere int, AnzStein int,AnzEchse int, AnzSpock int, AnzPapier int)")
    AnzSchere = data.get("Results").get("Schere")
    AnzStein = data.get('Results').get("Stein")
    AnzEchse = data.get('Results').get("Echse")
    AnzSpock = data.get('Results').get("Spock")
    AnzPapier = data.get('Results').get("Papier")
    cursor.execute("Select name from sqlite_master where type='table'")
    tables = cursor.fetchall()
    for t in tables:
        cursor.execute(f"Delete from {t[0]}")
    cursor.execute("Insert into Gamedata values (?,?,?,?,?)",(AnzSchere,AnzStein,AnzEchse,AnzSpock,AnzPapier))
    connection.commit()
    connection.close()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


