from fastapi import FastAPI, HTTPException
from app.chatbot import get_chatbot_response, ChatRequest

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Chatbot Backend"}

@app.post("/chat")
def chat(chat_request: ChatRequest):
    try:
        response = get_chatbot_response(chat_request.user_input)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
