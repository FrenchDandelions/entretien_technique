from flask import request, jsonify
from flask import Blueprint
from database import get_db, close_db
from utils import generate_short_id

"""
It'd be better to put the blueprints inside a Blueprint
directory but since we only have 1 it's fine for now
"""
bp = Blueprint('routes', __name__)


@bp.post('/encode')
def encode_url():
    data = request.get_json()
    #check if JSON data is present and contains the 'url' key
    if not data or 'url' not in data:
        return jsonify(error='Missing "url" in request'), 400

    original_url = data['url']
    short_id = generate_short_id(original_url)

    db = get_db()
    existing = db.execute('SELECT * FROM urls WHERE short = ?', (short_id,)).fetchone()
    #insert the URL only if it doesn't already exist in the database
    if not existing:
        db.execute(
            'INSERT OR IGNORE INTO urls (short, original) VALUES (?, ?)',
            (short_id, original_url)
        )
        db.commit()

    return jsonify(short_url=f'http://short.est/{short_id}')

# We keep it as a post method but it'd be better to make it a get
# method and have the short_url as a query string param since
# this endpoint only retrieves data 
@bp.post('/decode')
def decode_url():
    # Implementation using GET:
    # data = request.args.get('short_url')
    # if not data:
        # return jsonify(error="Missing "short_url" in request"), 400
    data = request.get_json()
    if not data or 'short_url' not in data:
        return jsonify(error='Missing "short_url" in request'), 400

    short_id = data['short_url'].split('/')[-1]
    db = get_db()
    row = db.execute('SELECT original FROM urls WHERE short = ?', (short_id,)).fetchone()
    if row:
        return jsonify(original_url=row['original'])
    return jsonify(error='URL not found'), 404


def register_routes(app):
    app.register_blueprint(bp)
