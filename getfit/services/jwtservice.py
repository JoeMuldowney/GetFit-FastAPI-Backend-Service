import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError


from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

import os
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

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