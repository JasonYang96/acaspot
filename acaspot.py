from flask import Flask, render_template, request, redirect, url_for
from models import Users
import flask_login
app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

users = Users()

# flask-login functions

@login_manager.user_loader
def user_loader(user):
    if not users.user_exists(user):
        return None

    return users.get_user(user)

@login_manager.request_loader
def request_loader(request):
    user = request.form.get('user')
    if not users.user_exists(user):
        return None

    #TODO hash pw
    auth = request.form['pw'] == users.get_user(user)['pw']
    users.authenticate_user(user, auth)

    return users.get_user(user)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    user = request.form['user']
    if request.form['pw'] == users.get_user(user)['pw']: 
        #flask_login.login_user(users.get_user(user))
        return redirect(url_for('profile', user=users.get_user(user)))

    flash('Bad login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    user = request.form['user']
    if (users.user_exists(user)):
        flash('User already exists')
        return

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

    users.add_user(user, pw, name, email, number, voice_part, sing_exp, music_exp, year, major, time_commit)
    #flask_login.login_user(users.get_user(user))
    return redirect(url_for('profile', user=users.get_user(user)))
@flask_login.login_required
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'GET':
        return render_template('profile.html', user=users[current_user.user])

    #TODO edit profile fields
    pass

@app.route('/logout')
@flask_login.login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
