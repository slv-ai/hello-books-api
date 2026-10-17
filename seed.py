from app import create_app,db
from app.models.book import Book

my_app = create_app()
books = [
    {
        "title": "The Secret Garden",
        "description": "A young girl discovers a hidden garden that changes her life."
    },
    {
        "title": "The Midnight Library",
        "description": "A woman explores different versions of her life through a mysterious library."
    },
    {
        "title": "The Lost Kingdom",
        "description": "An adventurer searches for a forgotten kingdom filled with secrets."
    },
    {
        "title": "A Journey Through Time",
        "description": "A scientist travels through time and discovers unexpected consequences."
    },
    {
        "title": "The Last Dragon",
        "description": "A young hero sets out to find the last dragon in a magical world."
    },
    {
        "title": "Mystery at Maple Street",
        "description": "A curious detective investigates strange events in a quiet neighborhood."
    },
    {
        "title": "The Ocean's Secret",
        "description": "A marine biologist discovers a hidden mystery beneath the ocean."
    },
    {
        "title": "Beyond the Stars",
        "description": "A group of explorers travels across the galaxy in search of a new home."
    },
    {
        "title": "The Art of Starting Over",
        "description": "A woman rebuilds her life after moving to a new city."
    },
    {
        "title": "The Forgotten Letter",
        "description": "An old letter reveals a family secret that was hidden for decades."
    }
]
# create_app() creates your Flask application.
# my_app.app_context() provides the application context needed to access Flask-SQLAlchemy.
with my_app.app_context():
    for book_data in books:
        book = Book(
            title = book_data["title"],
            description = book_data["description"]
            )
        db.session.add(book)
    db.session.commit()
    print(f"successfully added {len(books)} books")
# db.session.add() stages each cat for insertion.
# db.session.commit() saves the changes to the database.