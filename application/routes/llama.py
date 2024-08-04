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
    model_name = "gpt-4o-mini"
    user_input = request.input

    try:
        query_engine = index.as_query_engine()
        context = query_engine.query(user_input).response
        role = "You are a helpful student service chatbot, and you have been tasked in helping the student find an answer to their question. All the information you need has beenplaced in the context prompt and you should find a way to correlate the information you find there with thequestion of the User."

        prompt = f"Context: {context}\n\n Role: {role} \n\n User: {user_input}"
        
        print(prompt)

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-4o-mini",
        )
        message = response.choices[0]
    # except openai.error.OpenAIError as e:
    #     raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"response": message}