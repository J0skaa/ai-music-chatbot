from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from pydantic import BaseModel
import requests

class ChatRequest(BaseModel):
    user_input: str

MODEL_NAME = "microsoft/DialoGPT-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

API_KEY = "301fb7553c083663c800446045a6248c"
API_URL = "http://ws.audioscrobbler.com/2.0/"

def get_chatbot_response(user_input: str) -> str:
    """
    Generate a response using the chatbot or fetch music information.
    """
    if "music" in user_input.lower():
        params = {
            "method": "artist.search",
            "artist": user_input,
            "api_key": API_KEY,
            "format": "json"
        }
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            results = response.json()
            artists = results.get("results", {}).get("artistmatches", {}).get("artist", [])
            if artists:
                return f"Found artists: {', '.join(artist['name'] for artist in artists[:5])}"
            else:
                return "No artists found for your query."
        else:
            return "Error fetching data from Last.FM API."
    else:
        new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
        chat_history_ids = model.generate(
            new_user_input_ids,
            max_length=200,
            pad_token_id=tokenizer.eos_token_id,
        )
        response = tokenizer.decode(chat_history_ids[:, new_user_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response
