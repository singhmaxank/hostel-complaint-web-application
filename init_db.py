import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect('database.db')

# 1. Create Users Table
connection.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        roll_number TEXT, 
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'student'
    )
''')

# 2. Inject Default Admin Account
cursor = connection.cursor()
cursor.execute("SELECT * FROM users WHERE email='admin@iilm.edu'")
if not cursor.fetchone():
    hashed_pw = generate_password_hash('Admin123')
    cursor.execute('''
        INSERT INTO users (full_name, email, password, role)
        VALUES ('System Admin', 'admin@iilm.edu', ?, 'admin')
    ''', (hashed_pw,))
    print("👑 Default Admin account created!")

# 3. Create Complaints Table (Same as before)
connection.execute('DROP TABLE IF EXISTS complaints')
connection.execute('''
    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        roll_number TEXT NOT NULL,
        college_email TEXT NOT NULL,
        hostel_name TEXT NOT NULL,
        room_number TEXT NOT NULL,
        issue_title TEXT NOT NULL,
        issue_description TEXT NOT NULL,
        status TEXT DEFAULT 'Pending',
        date_submitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

print("✅ Database initialized successfully!")
connection.commit()
connection.close()
