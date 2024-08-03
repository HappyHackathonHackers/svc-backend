from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from application.routes.llama import router as llama_router
from application.routes.human import router as human_router

app = FastAPI()

# Set up for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(llama_router, prefix="/llama", tags=["llama"])
app.include_router(human_router, prefix="/human", tags=["human"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Services Application"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)