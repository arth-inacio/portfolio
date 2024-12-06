import sqlite3

def save_to_db(contact):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            subject TEXT,
            message TEXT
        )
    ''')
    cursor.execute('''
        INSERT INTO contacts (name, email, phone, subject, message)
        VALUES (?, ?, ?, ?, ?)
    ''', (contact['name'], contact['email'], contact['phone'], contact['subject'], contact['message']))
    conn.commit()
    conn.close()
