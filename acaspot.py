from flask import Flask, render_template, request, redirect, url_for, flash
from models import Users
import flask_login
from forms import LoginForm
app = Flask(__name__)
app.secret_key = 'acaspot'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

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
    users[user].authenticated = request.form['pw'] == users[user].pw

    return users[user]

# routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # make sure user exists
        user = str(request.form['user'])
        if user not in users:
            flash('Invalid Username. Please try again')
            return redirect(url_for('login'))

        if form.pw.data == users[user].pw:
            flask_login.login_user(users[user], remember = form.remember_me.data)
            return redirect(request.args.get('next') or url_for('user', user=user))

    return render_template('login.html', form=form)

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
    return redirect(url_for('user', user=user))

@flask_login.login_required
@app.route('/user/<user>', methods=['GET', 'POST'])
def user(user):
    return render_template('profile.html', user=users[user])

@flask_login.login_required
@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
