def test_register_user(client):

    response = client.post(
        "/addmember",
        json={
            "username": "john123",
            "password": "secret",
            "passwordverify": "secret",
            "fname": "John",
            "lname": "Doe",
            "email": "john@test.com"
        }
    )
    print(response.json())

    assert response.status_code == 201