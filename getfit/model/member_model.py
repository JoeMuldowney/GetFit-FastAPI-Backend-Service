from sqlalchemy import Column, Integer, String
from getfit.db.connection import Base

class Members(Base):
    __tablename__ = "member"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    password = Column(String(512))
    fname = Column(String(100))
    lname = Column(String(100))
    email = Column(String(100))