from fastapi import APIRouter, Depends
from dependencies import get_token_header

router = APIRouter(
    dependencies=[Depends(get_token_header)],
)

@router.get("/")
async def read_human():
    return {"message": "Human route"}

@router.post("/chat")
async def chat_with_human(query: str):
    response = {"query": query, "response": "Human response"}
    return response