from flask import Flask, render_template, request, redirect, url_for, flash
from models import Users
import flask_login
app = Flask(__name__)
app.secret_key = 'acaspot'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

users = {}

# flask-login functions

@login_manager.user_loader
def user_loader(user):
    if user not in users:
        return None

    return users[user]

@login_manager.request_loader
def request_loader(request):
    user = request.form.get('user')
    if user not in users:
        return None

    #TODO hash pw
    users[user].authenticated = request.form['pw'] == users[user]['pw']

    return users[user]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # check if user exists
    user = str(request.form['user'])
    print users

    if user not in users:
        flash('User does not exist')
        return 'User does not exist'

    if request.form['pw'] == users[user].pw: 
        flask_login.login_user(users[user])
        return redirect(url_for('profile', user=users[user]))

    flash('Incorrect Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    user = str(request.form['user'])
    if user in users:
        return 'User already exists'

    #TODO hash pw
    pw = request.form['pw']
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    voice_part = request.form['voice_part']
    sing_exp = request.form['sing_exp']
    music_exp = request.form['music_exp']
    year = request.form['year']
    major = request.form['major']
    time_commit = request.form['time_commit']

    users[user] = Users(user, pw, name, email, number, voice_part, sing_exp, music_exp, year, major, time_commit)
    flask_login.login_user(users[user])
    return render_template('profile.html', user=users[user])

@flask_login.login_required
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'GET':
        return render_template('profile.html', user=current_user)

    #TODO edit profile fields
    return render_template('profile.html', user=users[user])

@app.route('/logout')
@flask_login.login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
