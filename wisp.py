from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return "Here's the home where you vote"

@app.route('/submit', methods=['POST'])
def submit_vote():
    return ''

@app.route('/results')
def results_page():
    return "Results shown here"

@app.route('/host')
def host_page():
    return "Host controls here"
