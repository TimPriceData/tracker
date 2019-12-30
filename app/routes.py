from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    users = {'username': 'Tim'}
    logs = [
        {
            'owner': {'username': 'Tim'},
            'record': '30 minutes shallow work'
        },
        {
            'owner': {'username': 'Tim'},
            'record': '60 minutes concentrated work'
        }
    ]
    return render_template('index.html', title='home', users=users, logs=logs)
