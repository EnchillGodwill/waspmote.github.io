from app import app
from flask import render_template

@app.route('/')
def index():
    user = {
        'name':'libelium'
    }
    return render_template('index.html', user = user)
