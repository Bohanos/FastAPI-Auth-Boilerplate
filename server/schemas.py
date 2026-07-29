from pydantic import BaseModel


class Register (BaseModel):
    username: str
    password: str


class Login (BaseModel):
    username: str
    password: str

# class otp_verify(BaseModel):
#     UUID: str    