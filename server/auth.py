from fastapi import APIRouter, HTTPException, Request
from pwdlib import PasswordHash
import jwt
from server.limiter import limiter
from schemas import Register, Login

router = APIRouter()

users = []

password_hash = PasswordHash.recommended()

SECRET_KEY = "my-secret-key"

@router.post("/register")
@limiter.limit("5/minute")
def register(request: Request, new_user: Register):
    for existing_user in users:
        if existing_user["username"] ==  new_user.username:
            raise HTTPException(
                status_code=400,
                detail=f"Username '{new_user.username}' already exists."
            )
        
    hashed_password = password_hash.hash(new_user.password)

    users.append(
        {
            "username": new_user.username,
            "password": hashed_password
        }
    )

    return{
        "message": "Registration successful"
    }


@router.post("/Login")
@limiter.limit("5/minute")
def login(request: Request, user: Login):
    for saved_user in users:

        if saved_user["username"] == user.username:

            password_valid = password_hash.verify(
                user.password,
                saved_user["password"]
            )

            if password_valid:

                token = jwt.encode(
                    {
                        "username": user.username
                    },
                    SECRET_KEY,
                    algorithm = "HS256"
                )

                return{
                    "message": "Login successful",
                    "access_token": token
                }

    raise HTTPException(
        status_code=401,
        detail="Invalid username or password"
    )      