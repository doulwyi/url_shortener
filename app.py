from flask import Flask
from flask_restful import Api

from resources.url_shortener import UrlShorten, GetUrlShorten

app = Flask(__name__)

app.config.update()
app.secret_key = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # This should be modified in prod env.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(GetUrlShorten, '/<string:_hash>')
api.add_resource(UrlShorten, '/shorten_url/')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run()
