from sqlalchemy import func, case
from migrations import Country, Olympic, Result, Event, db, Player

# Query 1: For Olympic Games 2004 (birth year, player count, gold medal count)
def olympics_2004():
    results = db.session.query(
        func.extract('year', Player.birthdate).label('birth_year'),
        func.count(Player.player_id).label('num_players'),
        func.count(case([(Result.medal == 'GOLD', 1)], else_=0)).label('num_gold_medals')
    ).join(Result, Player.player_id == Result.player_id) \
        .join(Event, Result.event_id == Event.event_id) \
        .join(Olympic, Event.olympic_id == Olympic.olympic_id) \
        .filter(Olympic.year == 2004) \
        .group_by('birth_year').all()

    # Convert the query result to a list of dictionaries
    data = [
        {
            'birth_year': str(row.birth_year),
            'num_players': row.num_players,
            'num_gold_medals': row.num_gold_medals
        }
        for row in results
    ]

    return data

# Query 2: List Individual Events with Ties
def individual_event_ties():
    results = db.session.query(Event.name) \
        .join(Result).filter(Result.medal == 'GOLD', Event.is_team_event == 0) \
        .group_by(Event.name) \
        .having(func.count(Result.player_id) > 1).all()

    data = [{'event_name': row.name} for row in results]
    return data

# Query 3: Find Players Who Won Any Medal
def medalists():
    results = db.session.query(Player.name, Olympic.olympic_id) \
        .join(Result).join(Event).join(Olympic) \
        .filter(Result.medal.in_(['GOLD', 'SILVER', 'BRONZE'])).all()

    data = [{'player_name': row.name, 'olympic_id': row.olympic_id} for row in results]
    return data

# Query 4: Country with the Highest Percentage of Players with Vowel Names
def vowel_name_percentage():
    results = db.session.query(
        Country.name,
        func.count(Player.player_id).label('num_players'),
        func.count(case(
            (Player.name.ilike('A%'), 1),
            (Player.name.ilike('E%'), 1),
            (Player.name.ilike('I%'), 1),
            (Player.name.ilike('O%'), 1),
            (Player.name.ilike('U%'), 1),
            else_=0
        )).label('num_vowel_names')
    ).join(Player).group_by(Country.name).order_by(
        (func.count(case(
            (Player.name.ilike('A%'), 1),
            (Player.name.ilike('E%'), 1),
            (Player.name.ilike('I%'), 1),
            (Player.name.ilike('O%'), 1),
            (Player.name.ilike('U%'), 1),
            else_=0
        )) / func.count(Player.player_id)).desc()
    ).limit(1).all()

    data = [{'country_name': row.name, 'num_players': row.num_players, 'num_vowel_names': row.num_vowel_names} for row in results]
    return data

# Query 5: Find 5 Countries with Lowest Team-Medal-to-Population Ratio for 2000 Olympics
def team_medal_ratio():
    results = db.session.query(
        Country.name,
        func.count(Result.medal).label('team_medals'),
        Country.population
    ).select_from(Country) \
        .join(Player, Player.country_id == Country.country_id) \
        .join(Result, Result.player_id == Player.player_id) \
        .join(Event, Event.event_id == Result.event_id) \
        .join(Olympic, Olympic.olympic_id == Event.olympic_id) \
        .filter(Event.is_team_event == 1, Olympic.year == 2000) \
        .group_by(Country.name, Country.population) \
        .order_by((func.count(Result.medal) / Country.population).asc()) \
        .limit(5).all()

    data = [{'country_name': row.name, 'team_medals': row.team_medals, 'population': row.population} for row in results]
    return data
