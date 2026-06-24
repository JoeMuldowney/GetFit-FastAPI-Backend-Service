from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

import os
load_dotenv()

DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBHOST = os.getenv("DBHOST")
DBNAME = os.getenv("DBNAME")
DBPORT = os.getenv("DBPORT")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DBUSER}:{DBPASS}@{DBHOST}:{DBPORT}/{DBNAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()