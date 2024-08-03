from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from firebase.firebase import create_user, get_user, get_user_by_email, verify_id_token

router = APIRouter()


class User(BaseModel):
    email: str
    password: str


@router.post("/create_user")
async def post_create_user(request: User):
    user = create_user(request.email, request.password)
    return user


@router.get("/get_user/{uid}")
async def get_user(uid: str):
    user = get_user(uid)
    return user


@router.get("/get_user_by_email/{email}")
async def get_user_by_email(email: str):
    user = get_user_by_email(email)
    return user


@router.post("/verify_token")
async def verify_token(token: str):
    user = verify_id_token(token)
    return user
