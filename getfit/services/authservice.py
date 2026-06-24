from getfit.repository.members_repo import PersonRepository
from getfit.dto.authapi import MemberRegister, PersonFind
from getfit.services.jwtservice import create_access_token
from pwdlib import PasswordHash

class PersonService:
    def __init__(self, repo: PersonRepository):
        self.repo = repo
        self.password_hash = PasswordHash.recommended()

    def register_member(self, person: MemberRegister):
        if not person.username or not person.password or not person.email or not person.fname or not person.lname or not person.passwordverify:
            raise ValueError("all form fields are required")
        if person.password != person.passwordverify:
            raise ValueError("passwords do not match")
        verification = self.repo.verifyusername(person.username)
        if verification:
            raise ValueError("username already registered")
        hashed_pwd = self.password_hash.hash(person.password)
        return self.repo.create(person.username, hashed_pwd, person.fname, person.lname, person.email)

    def get_person_by_auth(self, person: PersonFind):
        if not person.username or not person.password:
            raise ValueError("username and password required")

        user = self.repo.get_by_auth(person.username)
        if user is None:
            raise ValueError("Invalid username or password")

        if not self.password_hash.verify(person.password, user.password):
            raise ValueError("Invalid username or password")

        token = create_access_token({
            "sub": str(user.id),
            "username": user.username,
            "fname": user.fname,
            "lname": user.lname,
        })

        return {
            "access_token": token,
            "token_type": "bearer"
        }
