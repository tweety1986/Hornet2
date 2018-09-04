from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
import sqlite3
import os
import hashlib


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(minutes=5)


def hash_passwd(hashed_password):
    hash_pass = hashlib.sha3_512(hashed_password.encode()).hexdigest()
    return hash_pass

def check_password(hashed_password, user_password):
    return hashed_password == hashlib.sha3_512(user_password.encode()).hexdigest()


def validate(username, password):
    con = sqlite3.connect('static/user.db')
    completion = False
    with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    db_user = row[1]
                    db_pass = row[2]
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
        with sqlite3.connect("static/user.db") as db:
            cursor = db.cursor()
        cursor.execute('SELECT pesel, name, surname, birth, grupa FROM dzieci')
        data = cursor.fetchall()
        db.commit()
    return render_template("profil.html", data=data, the_title='BAZA PRZEDSZKOLAKA')


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
            session['logged_in'] = username
            info = "ole" + " " + username
            flash(info)

            with sqlite3.connect("static/user.db") as db:
                cursor = db.cursor()
            cursor.execute('SELECT pesel, name, surname, birth, grupa FROM dzieci')
            data = cursor.fetchall()
            db.commit()
            return render_template('profil.html', error=error,data=data, the_chuj=username)
    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session.clear()
    return redirect(url_for('index'))


@app.route('/child', methods=['GET', 'POST'])
def child():
    if not session.get('logged_in'):

        return redirect(url_for('login'))
    if request.method == 'POST':

        with sqlite3.connect("static/user.db") as db:
            cursor = db.cursor()

        cursor.execute(
            'INSERT INTO dzieci (pesel, name, surname, birth, grupa) VALUES (?, ?, ?, ?, ?)',
            (
                request.form.get('pesel', type=int),
                request.form.get('name', type=str),
                request.form.get('surname', type=str),
                request.form.get('birth', type=str),
                request.form.get('grupa', type=str)
            )
        )
        db.commit()
        return redirect(url_for('child'))
    return render_template("child.html", the_title='BAZA PRZEDSZKOLAKA')


@app.route('/register', methods=['GET', 'POST'])

def register():

    if request.method == 'POST':

        with sqlite3.connect("static/user.db") as db:
            cursor = db.cursor()

        cursor.execute(
            'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
            (
                request.form.get('username', type=str),
                hash_passwd(request.form.get('password', type=str)),
                request.form.get('email', type=str))
        )
        db.commit()
        return redirect(url_for('register'))
    return render_template("register.html", the_title='BAZA PRZEDSZKOLAKA')



@app.route('/secret')
def secret():
    if not session.get('loged_in'):
        flash('You Not loged in')
        return redirect(url_for('login'))
    else:
        return "Hello Boss!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8060)
