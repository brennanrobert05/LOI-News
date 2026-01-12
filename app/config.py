import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api-football-v1.p.rapidapi.com/v3"


HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

if not API_KEY:
    raise ValueError("API_KEY not found")