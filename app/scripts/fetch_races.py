import requests
import json
from app.models import db, Race
from app import app

def save_races():
    response = requests.get("https://www.dnd5eapi.co/api/2014/races")
    races_list = response.json()['results']

    with app.app_context():
        for race_summary in races_list:
            full_race_response = requests.get(f"https://www.dnd5eapi.co{race_summary['url']}")
            race_data = full_race_response.json()

            race = Race(
                index=race_data["index"],
                name=race_data["name"],
                speed=race_data.get("speed"),
                ability_bonuses=json.dumps(race_data.get("ability_bonuses")),  # serialize lists
                age=race_data.get("age"),
                alignment=race_data.get("alignment"),
                size=race_data.get("size"),
                size_description=race_data.get("size_description"),
                starting_proficiencies=json.dumps(race_data.get("starting_proficiencies")),  # serialize
                languages=json.dumps(race_data.get("languages")),  # serialize
                language_desc=race_data.get("language_desc"),
                traits=json.dumps(race_data.get("traits")),  # serialize
                subraces=json.dumps(race_data.get("subraces")),  # serialize
                url=race_data.get("url")
            )

            db.session.add(race)
            
        db.session.commit()
        print("✔️ Races Seeded!")
if __name__ == "__main__":
    save_races()