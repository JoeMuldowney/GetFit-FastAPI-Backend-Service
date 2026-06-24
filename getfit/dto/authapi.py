from pydantic import BaseModel

class MemberRegister(BaseModel):
    username: str
    password: str
    passwordverify: str
    fname: str
    lname: str
    email: str

class RegisterResponse(BaseModel):
    id: int
    username: str
    fname: str

    class Config:
        orm_mode = True

class PersonFind(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True

class MemberResponse(BaseModel):
    username: str
    fname: str
    lname: str