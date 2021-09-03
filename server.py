from flask import Flask, request, redirect, render_template, session
import random
app = Flask(__name__)
app.secret_key = 'ih21oi3yh13uhibsday79u2b'

@app.route('/')
def index():
    # Count the number of guesses
    if 'count' not in session:
        session['count'] = 0
    print(session['count'])
    if 'num' not in session:
        session['num'] = random.randint(0,100)
    print(session['num'])
    if session['count'] == 6:
        reset_game()
    return render_template("index.html")

@app.route('/check', methods=['POST'])
def check_guess():
    # increase guess count
    session['count'] += 1
    if request.form['guess'].isdigit():
        session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset_game():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)