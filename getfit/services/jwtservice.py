import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError


from datetime import datetime, timedelta, timezone

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

SECRET_KEY = get_config("SECRETKEY")
ALGORITHM = get_config("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 130

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="findmember"
)



def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )


        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(401)

        return int(user_id)

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token expired"
        )
    except InvalidTokenError:
        raise HTTPException(
            401,
            "Invalid token"
        )

def get_current_user_data(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {
            "user_id": int(user_id),
            "username": payload.get("username"),
            "fname": payload.get("fname"),
            "lname": payload.get("lname"),
        }

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")