def test_get_all_books_with_no_records(client):

    #ACT
    response = client.get("/books")
    response_body = response.get_json()

    #ASSERT
    assert response.status_code == 200
    assert response_body == []

def test_get_all_books_with_two_records(client,two_saved_books):
    #act
    response = client.get("/books")
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body[0] == {
            "id" : 2,
            "title" : "mountain book",
            "description" : "2 climb rocks"
        }
    assert response_body[1] == {
        "id" : 1,
        "title" : "ocean book" ,
        "description" : "watever 4ever"
    }
    

def test_get_all_books_with_title_query_matching_none(client,two_saved_books):
    #Act
    data ={"title" : 'desert'}
    response = client.get("/books", query_string = data)
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_books_with_title_query_matching_one(client,two_saved_books):
    #Act
    data ={"title" : 'ocean book'}
    response = client.get("/books", query_string = data)
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
            "id" : 1,
            "title" : "ocean book" ,
            "description" : "watever 4ever"
        }

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


def test_get_one_book_missing_record(client, two_saved_books):
    # Act
    response = client.get("/books/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"Book 3 not found"}

def test_get_one_book_invalid_id(client, two_saved_books):
    # Act
    response = client.get("/books/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message":"Book cat invalid"}

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

def test_create_one_book_with_no_title(client):
    #arrange
    test_data ={ "description" : "the best!"}

    #act
    response = client.post("/books" , json = test_data)
    response_body = response.get_json()
    
    #assert
    assert response.status_code == 400
    assert response_body == {"message" : "Invalid request : missing title"}

def test_create_one_book_with_no_description(client):
    #arrange
    test_data ={ "title" : "new book!"}

    #act
    response = client.post("/books" , json = test_data)
    response_body = response.get_json()
    
    #assert
    assert response.status_code == 400
    assert response_body == {"message" : "Invalid request : missing description"}

def test_create_one_book_with_extra_keys(client):
    #arrange
    test_data ={ 
        "extra" : "some stuff",
        "title" : "new book",
        "description" : "the best!",
        "another" : "value"
        }

    #act
    response = client.post("/books" , json = test_data)
    response_body = response.get_json()
    
    #assert
    assert response.status_code == 201
    assert response_body == {
        "id" : 1,
        "title" : "new book",
        "description" : "the best!"
    }

def test_update_book(client, two_saved_books):
    # Arrange
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    response = client.put("/books/1", json=test_data)

    # Assert
    assert response.status_code == 204
    assert response.content_length is None

def test_update_book_with_extra_keys(client, two_saved_books):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "title": "New Book",
        "description": "The Best!",
        "another": "last value"
    }

    # Act
    response = client.put("/books/1", json=test_data)

    # Assert
    assert response.status_code == 204
    assert response.content_length is None

def test_update_book_missing_record(client, two_saved_books):
    # Arrange
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    response = client.put("/books/3", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Book 3 not found"}

def test_update_book_invalid_id(client, two_saved_books):
    # Arrange
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    response = client.put("/books/cat", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Book cat invalid"}

def test_delete_book(client, two_saved_books):
    # Act
    response = client.delete("/books/1")

    # Assert
    assert response.status_code == 204
    assert response.content_length is None

def test_delete_book_missing_record(client, two_saved_books):
    # Act
    response = client.delete("/books/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Book 3 not found"}

def test_delete_book_invalid_id(client, two_saved_books):
    # Act
    response = client.delete("/books/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Book cat invalid"}
