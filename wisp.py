import os
from flask import Flask, redirect, render_template, request, url_for, json

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

    return redirect(url_for('results_page'))

@app.route('/results')
def results_page():
    return render_template('results.html', results=votes)

@app.route('/host')
def host_page():
    return "Host controls here"
