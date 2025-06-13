from flask import g, current_app
import sqlite3

def get_db():
    """
    Retrieves the database connection from the application context.
    Creates a new connection if one does not already exist for the current request.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

# this function is called during the teardown context and receives
# an 'exception' parameter to handle exceptions differently if needed
def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            short TEXT PRIMARY KEY,
            original TEXT
        )
    ''')
    db.commit()
