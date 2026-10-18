from flask import abort, make_response
from ..db import db
def validate_book(cls,book_id):
    try:
        book_id = int(book_id)
    except:
        response = {"message" : f"{cls.__name__} {book_id} invalid"}
        abort(make_response(response,400))

    query = db.select(cls).where(cls.id == book_id)
    book = db.session.scalar(query)

    if not book:
        response = {"message" : f"{cls.__name__} {book_id} not found"}
        abort(make_response(response,404))
    return book