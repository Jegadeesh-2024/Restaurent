from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# Database connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",  # use your MySQL password if set
    "database": "restaurent-website"
}

@app.route("/reservations", methods=["GET"])
def show_reservations():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM hotel")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(rows)


@app.route("/reserve", methods=["POST"])
def reserve():
    data = request.json
    name = data["name"]
    email = data["email"]
    reservation_datetime = data["reservation_datetime"]
    people = data["people"]

    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    sql = "INSERT INTO hotel (name, email, reservation_datetime, people) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, email, reservation_datetime, people))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Reservation successful!"})

if __name__ == "__main__":
    app.run(debug=True)
