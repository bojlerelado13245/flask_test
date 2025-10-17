from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the parent folder of Backend/ to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Database import db  # now Python can find db.py

app = Flask(__name__)
CORS(app)  # enable cross-origin requests

db.init_db()  # ensure the database and table exist

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    username = data.get('username', '')
    email = data.get('email', '')

    db.save_user(username, email)  # save to SQLite

    return jsonify(message="Saved!", username=username, email=email)

@app.route('/get_sql', methods=['GET'])
def get_sql():
            sql_data = db.get_all_users()
            return jsonify(sql_data)

if __name__ == '__main__':
    app.run(debug=True)
