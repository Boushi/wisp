from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def home_page():
    games = [
        {
            "name": "werewolf",
            "players": 8
        },
        {
            "name": "catan",
            "players": 5
        },
    ]
    return render_template('home.html', games=games)

@app.route('/submit', methods=['POST'])
def submit_vote():
    return request.form

@app.route('/results')
def results_page():
    return "Results shown here"

@app.route('/host')
def host_page():
    return "Host controls here"
