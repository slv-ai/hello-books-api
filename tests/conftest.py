import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.book import Book
from app.models.author import Author
from app.models.genre import Genre

@pytest.fixture
def app():
    test_config ={
        "TESTING" : True,
        "SQLALCHEMY_DATABASE_URI" : os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    }
    app =create_app(test_config)

    @request_finished.connect_via(app) #DECORATOR INDICATES THE FUNCTION DEFINED BELOW WILL BE INVOKED AFTER ANY REQUEST COMPLETED
    def expire_session(sender,response,**extra):
        db.session.remove()
    with app.app_context():
        db.create_all()
        yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_books(app):
    ocean_book = Book(title = "ocean book" ,
                    description = "watever 4ever")
    
    mountain_book = Book(title = "mountain book",
                        description = "2 climb rocks")
    db.session.add_all([ocean_book,mountain_book])
    db.session.commit()

@pytest.fixture
def one_saved_author(app):
    author = Author(name="New Author 1")
    db.session.add(author)
    db.session.commit()
@pytest.fixture
def author_with_two_books(app, one_saved_author):    
    desert_book = Book(title="Desert Book",
                    description="Sands all around",
                    author_id=1)
    plains_book = Book(title="Plains Book",
                    description="Grasslands for miles",
                    author_id=1)

    db.session.add_all([desert_book, plains_book])
    db.session.commit()

@pytest.fixture
def one_saved_genre(app):
    genre = Genre(name="New Genre 1")
    db.session.add(genre)
    db.session.commit()

    return genre


@pytest.fixture
def genre_with_two_books(app, one_saved_genre):   
    sky_book = Book(title="Sky Book",
                    description="Floating in the clouds",
                    genres=[one_saved_genre])
    tundra_book = Book(title="Tundra Book",
                    description="Like plains but colder",
                    genres=[one_saved_genre])

    db.session.add_all([sky_book, tundra_book])
    db.session.commit()