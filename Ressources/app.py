from flask import Flask, jsonify, request
import hashlib
import sqlite3

app = Flask(__name__)

# SQLite database connection
def get_db_connection():
    conn = sqlite3.connect('urls.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create table if it doesn't exist
def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS urls (short TEXT, original TEXT)')
    conn.commit()
    conn.close()

init_db()

# Function to generate a short identifier
def generate_short_id(url):
    return hashlib.sha256(url.encode()).hexdigest()[:6]

# Endpoint to encode a URL
@app.route('/encode', methods=['POST'])
def encode_url():
    original_url = request.json['url']
    short_id = generate_short_id(original_url)
    conn = get_db_connection()
    conn.execute('INSERT INTO urls (short, original) VALUES (?, ?)', (short_id, original_url))
    conn.commit()
    conn.close()
    return jsonify(short_url=f'http://short.est/{short_id}')

# Endpoint for URL decoding
@app.route('/decode', methods=['POST'])
def decode_url():
    short_id = request.json['short_url'].split('/')[-1]
    conn = get_db_connection()
    url_data = conn.execute('SELECT original FROM urls WHERE short = ?', (short_id,)).fetchone()
    conn.close()
    if url_data:
        return jsonify(original_url=url_data['original'])
    else:
        return jsonify(error='URL not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
