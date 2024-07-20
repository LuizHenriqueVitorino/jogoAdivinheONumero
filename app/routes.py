from flask import render_template, request, redirect, url_for, session
import random

from . import create_app

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        guess = int(request.form['guess'])
        target = session.get('target')
        
        if target is None:
            target = random.randint(1, 100)
            session['target'] = target
        
        if guess < target:
            feedback = "Too low!"
        elif guess > target:
            feedback = "Too high!"
        else:
            feedback = "Correct!"
            session.pop('target', None)  # Reset the game
        
        return render_template('result.html', feedback=feedback)
    
    return render_template('index.html')

@app.route('/error')
def error():
    return render_template('error.html')
