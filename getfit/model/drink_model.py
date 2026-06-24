from sqlalchemy import Column, Integer, String, Float, DateTime
from getfit.db.connection import Base


class Drinks(Base):
    __tablename__ = "drink"

    id = Column(Integer, primary_key=True, index=True)
    drinkname = Column(String(100))
    drinkamount = Column(Float)
    daytime = Column(DateTime)