from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user={'username': 'Andre'}
    posts= [
        {
            'author': {'username': 'Andre'},
            'body': 'So bored in lockdown!'
        },
        {
            'author':{'username': 'Madison'},
            'body': 'Tell me about it!'
        },
        {
            'author': {'username': 'Max'},
            'body': 'Hurry up and finish your work'
        }
    ]
    return render_template('index.html', posts=posts, user=user)