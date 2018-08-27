from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
import sqlite3
import os
import hashlib


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=2)


def check_password(hashed_password, user_password):
    return hashed_password == hashlib.md5(user_password.encode()).hexdigest()


def validate(username, password):
    con = sqlite3.connect('static/user.db')
    completion = False
    with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    db_user = row[0]
                    db_pass = row[1]
                    if db_user == username:
                        completion = check_password(db_pass, password)
    return completion


@app.route('/')
def index():

    return render_template('base.html', the_title="BAZA PRZEDSZKOLAKA")


@app.route('/profil')
def profil():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template("profil.html", the_title='BAZA PRZEDSZKOLAKA')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion is False:
            error = 'Niepoprawny login lub hasło'
        else:
            session['logged_in'] = True
            return redirect(url_for('profil'))

    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=0)
    return redirect(url_for('index'))

@app.route('/child')
def child():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template("child.html", the_title='BAZA PRZEDSZKOLAKA')


@app.route('/secret')
def secret():
    if not session.get('loged_in'):
        return redirect(url_for('login'))
    else:
        return "Hello Boss!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8060)
