from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
import sqlite3

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

@app.route('/update', methods=['PUT'])
def update_user():
            data = request.get_json()
            userid = data.get('userid', None)
            username = data.get('username', '')
            email = data.get('email', '')
            if userid is None:
                        return jsonify(message="Error: User ID is required."), 400
            # Update user in the database
            conn = sqlite3.connect(db.DB_PATH)
            conn.execute('UPDATE users SET username = ?, email = ? WHERE id = ?', (username, email, userid))
            conn.commit()
            conn.close()
            return jsonify(message=f"User with ID {userid} updated.", username=username, email=email)

@app.route('/delete', methods=['DELETE'])
def delete_user():
            data = request.get_json()
            userid = data.get('userid', None)
            if userid is None:
                        return jsonify(message="Error: User ID is required."), 400
            db.delete_user(userid)
            return jsonify(message=f"User with ID {userid} deleted.")

if __name__ == '__main__':
    app.run(debug=True)
