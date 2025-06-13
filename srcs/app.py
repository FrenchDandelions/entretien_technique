from flask import Flask
from database import init_db, close_db
from routes import register_routes

app = Flask(__name__)
# It's better to store the database path inside an env variable
# to be able to configure / switch databases more easily if needed
app.config['DATABASE'] = 'urls.db'

# teardown handler to close db connection after each request
app.teardown_appcontext(close_db)

register_routes(app)

#Making sure that the database is initialized before
#handling the first request, and it runs within the
#app context, so current_app and g are available
@app.before_first_request
def init_database():
    init_db()

if __name__ == '__main__':
    # since we're supposedly in a production environnement
    # debug should be set to False instead of True
    app.run(debug=False)
