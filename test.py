from dotenv import load_dotenv
import os
from espn_api.football import League

# Load .env file
success = load_dotenv()
print(f".env loaded: {success}")

# Retrieve values
league_id = os.getenv("LEAGUE_ID")
year = os.getenv("YEAR")
swid = os.getenv("SWID")
espn_s2 = os.getenv("ESPN_S2")

print(f"LEAGUE_ID: {league_id}")
print(f"YEAR: {year}")
print(f"SWID: {swid[:8]}...")  # Only show part for security
print(f"ESPN_S2: {espn_s2[:8]}...")  # Only show part for security

try:
    league = League(league_id=int(league_id), year=int(year), swid=swid, espn_s2=espn_s2)
    print(f"✅ Connected to league: {league.settings.name}")
except Exception as e:
    print(f"❌ Could not fetch data from ESPN:\n{e}")
