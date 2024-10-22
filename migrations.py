from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Country(db.Model):
    __tablename__ = 'countries'
    country_id = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String(40))
    area_sqkm = db.Column(db.Integer)
    population = db.Column(db.Integer)

class Olympic(db.Model):
    __tablename__ = 'olympics'
    olympic_id = db.Column(db.String(7), primary_key=True)
    country_id = db.Column(db.String(3), db.ForeignKey('countries.country_id'))
    city = db.Column(db.String(50))
    year = db.Column(db.Integer)
    startdate = db.Column(db.Date)
    enddate = db.Column(db.Date)

class Player(db.Model):
    __tablename__ = 'players'
    player_id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(40))
    birthdate = db.Column(db.Date)
    country_id = db.Column(db.String(3), db.ForeignKey('countries.country_id'))

class Event(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.String(7), primary_key=True)
    name = db.Column(db.String(40))
    eventtype = db.Column(db.String(20))
    olympic_id = db.Column(db.String(7), db.ForeignKey('olympics.olympic_id'))
    is_team_event = db.Column(db.Integer)
    num_players_in_team = db.Column(db.Integer)
    result_noted_in = db.Column(db.String(100))

class Result(db.Model):
    __tablename__ = 'results'
    event_id = db.Column(db.String(7), db.ForeignKey('events.event_id'), primary_key=True)
    player_id = db.Column(db.String(10), db.ForeignKey('players.player_id'), primary_key=True)
    medal = db.Column(db.String(7))
    result = db.Column(db.Float)
