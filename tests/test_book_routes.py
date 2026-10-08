def test_get_all_books_with_no_records(client):

    #ACT
    response = client.get("/books")
    response_body = response.get_json()

    #ASSERT
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client,two_saved_books):
    #act
    response = client.get("/books/1")
    response_body = response.get_json()
    #assert
    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "title" : "ocean book",
        "description" : "watever 4ever"

    }
def test_create_one_book(client):
    #act
    response = client.post("/books", json = {
        "title" : "new book",
        "description" : "the best!"
    })
    response_body = response.get_json()
    #assert
    assert response.status_code == 201
    assert response_body == {
        "id" : 1,
        "title" : "new book",
        "description" : "the best!"
    }