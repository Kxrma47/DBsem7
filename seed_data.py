import random
from faker import Faker
from migrations import db, Country, Olympic, Player, Event, Result
from datetime import datetime

fake = Faker()

def seed_data(num_records):

    db.session.query(Result).delete()
    db.session.query(Event).delete()
    db.session.query(Player).delete()
    db.session.query(Olympic).delete()
    db.session.query(Country).delete()

    country_ids = set()

    for _ in range(num_records):
        country_id = fake.country_code()[:3]
        while country_id in country_ids:
            country_id = fake.country_code()[:3]
        country_ids.add(country_id)

        country = Country(
            country_id=country_id,
            name=fake.country(),
            area_sqkm=random.randint(10000, 100000),
            population=random.randint(1000000, 100000000)
        )
        db.session.add(country)
        print(f"Seeded Country: {country.name}")

    for _ in range(num_records // 10):
        olympic = Olympic(
            olympic_id=fake.bothify(text="O######"),
            country_id=random.choice(list(country_ids)),
            city=fake.city(),
            year=random.choice([2000, 2004]),
            startdate=datetime.strptime(fake.date(), '%Y-%m-%d').date(),
            enddate=datetime.strptime(fake.date(), '%Y-%m-%d').date()
        )
        db.session.add(olympic)
        print(f"Seeded Olympic: {olympic.city} {olympic.year}")

    for _ in range(num_records):
        player = Player(
            name=fake.name(),
            player_id=fake.bothify(text="P########"),
            country_id=random.choice(list(country_ids)),
            birthdate=fake.date_of_birth(minimum_age=18, maximum_age=40)
        )
        db.session.add(player)
        print(f"Seeded Player: {player.name}, Birthdate: {player.birthdate}")

    for _ in range(num_records // 5):
        event = Event(
            event_id=fake.bothify(text="E######"),
            name=fake.word().capitalize() + " Event",
            eventtype=random.choice(['Individual', 'Team']),
            olympic_id=random.choice(db.session.query(Olympic.olympic_id).all())[0],
            is_team_event=random.choice([0, 1]),
            num_players_in_team=random.randint(1, 5),
            result_noted_in="Seconds"
        )
        db.session.add(event)
        print(f"Seeded Event: {event.name}, Type: {event.eventtype}, Team Event: {event.is_team_event}")

    used_combinations = set()

    player_ids = db.session.query(Player.player_id).all()
    event_ids = db.session.query(Event.event_id).all()
    for _ in range(num_records):
        event_id = random.choice(event_ids)[0]
        player_id = random.choice(player_ids)[0]

        if (event_id, player_id) in used_combinations:
            continue

        used_combinations.add((event_id, player_id))

        result = Result(
            event_id=event_id,
            player_id=player_id,
            medal=random.choice(['GOLD', 'SILVER', 'BRONZE', None]),
            result=random.uniform(9.0, 100.0)
        )
        db.session.add(result)
        print(f"Seeded Result: Player {result.player_id} in {result.event_id} won {result.medal}")

    db.session.commit()
    print("Data seeded successfully!")