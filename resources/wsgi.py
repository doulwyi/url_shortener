from app import app
from db import db

if __name__ == '__main__':
    db.init_app(app)
    app.run()