import requests
from app.models import db, Race, CharClass, Background
from app import app

# What I want to fetch
wanted_races = ['elf', 'halfling', 'aasimar']
wanted_classes = ['rogue', 'cleric', 'druid']
wanted_backgrounds = ['acolyte', 'criminal', 'sage']

BASE_URL = "https://www.dnd5eapi.co/api/2014"

def fetch_list(endpoint, wanted_list):
    results = []
    response = requests.get(f"{BASE_URL}/{endpoint}")

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json().get('results', [])
        # Loops through the data and gets the item needed from the wanted_list, adding it to results
        for item in data:
            if item['index'] in wanted_list:
                results.append(item)

    else: 
        print(f"Error fetching {endpoint}: {response.status_code}")

    return results

def save_data():
    with app.app_context():
        # RACES
        races = fetch_list("races", wanted_races)
        if races:
            for race in races:
                existing = Race.query.filter_by(index=race['index']).first()
                if not existing:
                    new_race = Race(index=race['index'], name=race['name'])
                    db.session.add(new_race)
        else:
            print("No races data fetched.")

        # CLASSES
        classes = fetch_list("classes", wanted_classes)
        if classes:
            for char_class in classes:
                existing = CharClass.query.filter_by(index=char_class['index']).first()
                if not existing:
                    new_class = CharClass(index=char_class['index'], name=char_class['name'])
                    db.session.add(new_class)
        else:
            print("No classes data fetched.")

        # BACKGROUNDS
        backgrounds = fetch_list("backgrounds", wanted_backgrounds)
        if backgrounds:
            for bg in backgrounds:
                existing = Background.query.filter_by(index=bg['index']).first()
                if not existing:
                    new_bg = Background(index=bg['index'], name=bg['name'])
                    db.session.add(new_bg)
        else:
            print("No backgorunds data fetched.")

        db.session.commit()
        print("✔️ D&D data saved to the database!")

if __name__ == "__main__":
    save_data()