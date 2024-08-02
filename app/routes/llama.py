from fastapi import APIRouter, Depends
from dependencies import get_token_header

router = APIRouter(
    dependencies=[Depends(get_token_header)],
)

@router.get("/")
async def read_llama():
    return {"message": "Llama route"}

@router.post("/chat")
async def chat_with_llama(query: str):
    response = {"query": query, "response": "Llama response"}
    return response