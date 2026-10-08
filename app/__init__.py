from flask import Flask
#from .routes.hello_world_routes import hello_world_bp
from .routes.book_routes import books_bp
from .db import db
from .db import migrate
from .models import book
import os

def create_app(config = None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    if config :
        app.config.update(config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(books_bp)

    return app
    