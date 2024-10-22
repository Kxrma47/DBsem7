from flask import Flask, jsonify
from migrations import db
from seed_data import seed_data
from queries import olympics_2004, individual_event_ties, medalists, vowel_name_percentage, team_medal_ratio

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///olympics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return "Welcome to the Olympics API!"

@app.route('/seed')
def seed():
    seed_data(100)
    return "Data seeded successfully!"

@app.route('/olympics_2004', methods=['GET'])
def get_olympics_2004():
    data = olympics_2004()
    return jsonify(data)

@app.route('/individual_event_ties')
def get_individual_event_ties():
    data = individual_event_ties()
    return jsonify(data)

@app.route('/medalists')
def get_medalists():
    data = medalists()
    return jsonify(data)

@app.route('/vowel_name_percentage')
def get_vowel_name_percentage():
    data = vowel_name_percentage()
    return jsonify(data)

@app.route('/team_medal_ratio')
def get_team_medal_ratio():
    data = team_medal_ratio()
    return jsonify(data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
