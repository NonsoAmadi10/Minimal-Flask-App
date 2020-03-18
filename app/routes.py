from flask import render_template, flash, redirect
from .forms import LoginForm
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"name": "justice"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)


@app.route('/login', methods =['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'login requested for user {form.name.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='login', form=form)