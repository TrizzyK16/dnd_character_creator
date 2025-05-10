from app.models import db, Race, CharClass, Background
from app import app

def view_data():
    with app.app_context():
        print("\n📜 Races:")
        for race in Race.query.all():
            print(f"- {race.name} ({race.index})")

        print("\n🛡️ Classes:")
        for char_class in CharClass.query.all():
            print(f"- {char_class.name} ({char_class.index})")

        print("\n📖 Backgorunds:")
        for bg in Background.query.all():
            print(f"- {bg.name} ({bg.index})")

if __name__ == "__main__":
    view_data()