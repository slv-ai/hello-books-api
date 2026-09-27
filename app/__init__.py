from flask import Flask
#from .routes.hello_world_routes import hello_world_bp
from .routes.hello_world_routes import books_bp
def create_app():
    app = Flask(__name__)
    app.register_blueprint(books_bp)

    return app
    