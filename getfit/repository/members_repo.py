from sqlalchemy.orm import Session
from getfit.model.member_model import Members
from sqlalchemy import select
class PersonRepository:
    def __init__(self, db: Session):
        self.db = db
    # inserts a new user into the table
    def create(self, username: str, password: str, fname: str, lname: str, email: str):
        person = Members(username=username, password=password, fname=fname, lname=lname, email=email)
        self.db.add(person)
        self.db.commit()
        self.db.refresh(person)
        return person
    # verify username not already in use
    def verifyusername(self, username: str) -> bool:
        stmt = select(Members).where(Members.username == username)
        result = self.db.execute(stmt).scalars().first()
        return result is not None

    def get_by_auth(self, username: str) -> Members | None:
        stmt = select(Members).where(Members.username == username)
        user = self.db.execute(stmt).scalars().first()
        if not user:
            return None
        return user



