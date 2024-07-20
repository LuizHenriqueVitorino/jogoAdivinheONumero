from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

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
