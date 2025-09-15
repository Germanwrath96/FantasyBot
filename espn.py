import os
from espn_api.football import League
from dotenv import load_dotenv

load_dotenv()

def get_league():
    league_id = int(os.getenv("LEAGUE_ID"))
    year = int(os.getenv("YEAR"))
    swid = os.getenv("SWID")
    espn_s2 = os.getenv("ESPN_S2")

    return League(league_id=league_id, year=year, swid=swid, espn_s2=espn_s2)

def get_league_name():
    league = get_league()
    return league.settings.name
