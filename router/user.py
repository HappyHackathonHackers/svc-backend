from fastapi import APIRouter, HTTPException
from firebase.firebase import create_user, get_user, get_user_by_email, verify_id_token

router = APIRouter()


@router.post("/create_user")
async def create_user(email: str, password: str):
    user = create_user(email, password)
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
