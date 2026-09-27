from flask import Blueprint
from app.models.book import books
books_bp  = Blueprint("books_bp", __name__, url_prefix="/books")
@books_bp.get("/<book_id>")

def get_one_book(book_id):
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            return {
                "id" : book.id,
                "title" : book.title,
                "description" : book.description
            }


# def get_all_books():
#     books_response =[]
#     for book in books:
#         books_response.append(
#             {
#                 "id" : book.id,
#                 "title" : book.title,
#                 "description" : book.description

#             }
#         )
#     return books_response







# hello_world_bp = Blueprint("hello_world", __name__)
# @hello_world_bp.get("/")
# def say_hello_world():
#     return "Hello world"

# @hello_world_bp.get("/hello/JSON")
# def say_hello_json():
#     return {
#         "name" : "ADA",
#         "message" : "hello",
#         "hobbies" : ["fishing","swimming"]
#     }

# @hello_world_bp.get("/broken-endpoint-with-broken-servercode")
# def broken_endpoint():
#     response_body = {
#         "name" : "ADA",
#         "message" : "hello",
#         "hobbies" : ["fishing","swimming"]
#     }
#     new_hobby = "surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body

