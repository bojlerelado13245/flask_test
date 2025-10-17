import os
import sqlite3

# Database file path, always relative to db.py
DB_PATH = os.path.join(os.path.dirname(__file__), 'app.db')

def init_db():
    """Create the users table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_user(username, email):
    """Insert a new user into the database."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
    conn.commit()
    conn.close()

def get_all_users():
            """Retrieve all users from the database."""
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.execute('SELECT id, username, email FROM users')
            users = [{'id': row[0], 'username': row[1], 'email': row[2]} for row in cursor.fetchall()]
            conn.close()
            return users
