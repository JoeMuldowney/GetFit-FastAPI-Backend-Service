def test_register_user_success(client):

    response = client.post(
        "/api/addmember",
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

def test_register_user_fail(client):

    response = client.post(
        "/api/addmember",
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

    assert response.status_code == 403

def test_find_user_success(client):

    response = client.post(
        "/api/findmember",
        json={
            "username": "john123",
            "password": "secret"
        }
    )
    print(response.json())

    assert response.status_code == 200

def test_find_user_success_fail_password(client):

    response = client.post(
        "/api/findmember",
        json={
            "username": "john123",
            "password": "secret1"
        }
    )
    print(response.json())

    assert response.status_code == 403



