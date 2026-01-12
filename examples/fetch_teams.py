import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("API_KEY")
league = "League of Ireland First Division"

url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/search_all_teams.php?l={league}"

response = requests.get(url)
data = response.json()

for team in data.get("teams", []):
    print(team["strTeam"])
