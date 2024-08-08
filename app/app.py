from flask import Flask
import sqlite3

conn = sqlite3.connect('catcount.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS catcount (id INTEGER PRIMARY KEY, count INTEGER)')
# cursor.execute('INSERT INTO catcount (count) VALUES (2)')
conn.commit()
conn.close()

app = Flask(__name__)

@app.route('/')
def root_call():
    return "Hello World!"


@app.route('/get_cat_count', methods=['GET'])
def get_current_count():
    conn = sqlite3.connect('catcount.db')
    cursor = conn.cursor()
    cursor.execute('SELECT count FROM catcount WHERE id = 1')
    result = cursor.fetchone()
    conn.close()
    print('Count retrieved')
    if result:
        return str(result[0])
    else:
        return None


@app.route('/increment_cat_count', methods=['POST', 'GET'])
def increment_count():
    conn = sqlite3.connect('catcount.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE catcount SET count = count + 1 WHERE id = 1')
    conn.commit()
    conn.close()
    print('Count incremented')
    return "Count incremented"
