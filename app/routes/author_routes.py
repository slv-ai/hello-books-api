from flask import Blueprint, make_response, abort,request
from app.models.author import Author
from app.models.book import Book
from .route_utilities import validate_model , create_model, get_models_with_filters
from ..db import db

bp = Blueprint("autors_bp", __name__, url_prefix= "/authors")

@bp.post("")
def create_author():
    request_body = request.get_json()
    
    return create_model(Author,request_body)

@bp.get("")
def get_all_authors():
    
    return get_models_with_filters(Author, request.args)

