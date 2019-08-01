from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit_vote():
    return ''

@app.route('/results')
def results_page():
    return "Results shown here"

@app.route('/host')
def host_page():
    return "Host controls here"
