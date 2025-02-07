from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Body
from app.chatbot import get_chatbot_response, ChatRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Chatbot Backend"}
