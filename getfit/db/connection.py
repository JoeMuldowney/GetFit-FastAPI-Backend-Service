from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def get_config(name: str) -> str:
    secret = Path(f"/run/secrets/{name}")
    if secret.exists():
        return secret.read_text().strip()

    value = os.getenv(name)
    if value is None:
        raise RuntimeError(f"Missing configuration: {name}")

    return value

DBUSER = get_config("DBUSER")
DBPASS = get_config("DBPASS")
DBHOST = get_config("DBHOST")
DBPORT = get_config("DBPORT")
DBNAME = get_config("DBNAME")


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