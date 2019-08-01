import os
from flask import Flask, render_template, request, url_for, json

games = []
votes = {}

def create_app():
    app = Flask(__name__)
    games_list = json.load(open(os.path.join(app.root_path, 'games.json')))
    for game in games_list:
        games.append(game)
    return app

app = create_app()

@app.route('/')
def home_page():
    return render_template('home.html', games=games)

@app.route('/submit', methods=['POST'])
def submit_vote():
    for game in request.form:
        if game in votes:
            votes[game] = votes[game] + 1
        else:
            votes[game] = 1

    return votes

@app.route('/results')
def results_page():
    return "Results shown here"

@app.route('/host')
def host_page():
    return "Host controls here"
