# routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

router = APIRouter()

class ChatRequest(BaseModel):
    input: str

documents = SimpleDirectoryReader('./documents').load_data()
index = VectorStoreIndex.from_documents(documents)

@router.post("/chat")
async def chat(request: ChatRequest):
    model_name = "gpt-3.5-turbo"
    user_input = request.input

    try:
        query_engine = index.as_query_engine()
        context = query_engine.query(user_input).response

        prompt = f"Context: {context}\n\nUser: {user_input}"
        
        print(prompt)

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
        message = response.choices[0]
    # except openai.error.OpenAIError as e:
    #     raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"response": message}