from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from getfit.db.connection import Base

class Meals(Base):
    __tablename__ = "meal"

    id = Column(Integer, primary_key=True, index=True)
    foodname = Column(String(100))
    foodamount = Column(Float)
    daytime = Column(DateTime)
    user_id = Column(Integer, ForeignKey("member.id"))



