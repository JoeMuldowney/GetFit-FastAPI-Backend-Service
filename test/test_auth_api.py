from fastapi.testclient import TestClient

from getfit.main import (
    app,
    get_service,
    get_current_user_data
)

from getfit.dto.authapi import (
    MemberRegister,
    PersonFind
)

client = TestClient(app)


# ======================================================
# /addmember - SUCCESS
# ======================================================

class MockPersonServiceSuccess:
    def register_member(self, person: MemberRegister):
        return {
            "id": 1,
            "username": person.username,
            "fname": person.fname
        }


def test_add_member_success():
    app.dependency_overrides[get_service] = lambda: MockPersonServiceSuccess()

    payload = MemberRegister(
        username="john123",
        password="secret",
        passwordverify="secret",
        fname="John",
        lname="Doe",
        email="john@test.com"
    )

    response = client.post("/addmember", json=payload.model_dump())

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == 1
    assert data["username"] == "john123"
    assert data["fname"] == "John"

    app.dependency_overrides.clear()


# ======================================================
# /addmember - FAILURE
# ======================================================

class MockPersonServiceFail:
    def register_member(self, person: MemberRegister):
        raise ValueError("User already exists")


def test_add_member_failure():
    app.dependency_overrides[get_service] = lambda: MockPersonServiceFail()

    payload = MemberRegister(
        username="john123",
        password="secret",
        passwordverify="secret",
        fname="John",
        lname="Doe",
        email="john@test.com"
    )

    response = client.post("/addmember", json=payload.model_dump())

    assert response.status_code == 400
    assert response.json()["detail"] == "User already exists"

    app.dependency_overrides.clear()


# ======================================================
# /findmember - SUCCESS
# ======================================================

class MockLoginSuccess:
    def get_person_by_auth(self, person: PersonFind):
        return {
            "access_token": "fake-jwt-token",
            "token_type": "bearer"
        }


def test_find_member_success():
    app.dependency_overrides[get_service] = lambda: MockLoginSuccess()

    payload = PersonFind(
        username="john123",
        password="secret"
    )

    response = client.post("/findmember", json=payload.model_dump())

    assert response.status_code == 200
    data = response.json()

    assert data["access_token"] == "fake-jwt-token"
    assert data["token_type"] == "bearer"

    app.dependency_overrides.clear()


# ======================================================
# /findmember - FAILURE
# ======================================================

class MockLoginFail:
    def get_person_by_auth(self, person: PersonFind):
        raise ValueError("Invalid credentials")


def test_find_member_failure():
    app.dependency_overrides[get_service] = lambda: MockLoginFail()

    payload = PersonFind(
        username="john123",
        password="wrongpass"
    )

    response = client.post("/findmember", json=payload.model_dump())

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

    app.dependency_overrides.clear()


# ======================================================
# /me - SUCCESS
# ======================================================

def test_get_me():
    app.dependency_overrides[get_current_user_data] = lambda: {
        "username": "john123",
        "fname": "John",
        "lname": "Doe"
    }

    response = client.get("/me")

    assert response.status_code == 200
    data = response.json()

    assert data["username"] == "john123"
    assert data["fname"] == "John"
    assert data["lname"] == "Doe"

    app.dependency_overrides.clear()