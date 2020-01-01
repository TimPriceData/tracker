from flask import render_template, flash, url_for, redirect
from app import app
from app.forms import LoginForm

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)