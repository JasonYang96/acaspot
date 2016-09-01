from flask import Flask, render_template, request, redirect, url_for, flash
from models import Users
import flask_login
from forms import LoginForm, RegistrationForm
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
        user = form.user.data
        if user not in users:
            flash('Invalid Username. Please try again')
            return redirect(url_for('login'))

        if form.pw.data == users[user].pw:
            flask_login.login_user(users[user], remember=form.remember_me.data)
            return redirect(request.args.get('next') or url_for('user', user=user))

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = form.user.data
        if user in users:
            flash('User already exists. Please try again')
            return redirect(url_for('register'))

        #TODO hash pw
        pw = form.pw.data

        users[user] = Users(user, pw)
        flask_login.login_user(users[user])
        return redirect(url_for('user', user=user))

    return render_template('register.html', form=form)

@flask_login.login_required
@app.route('/user/<user>', methods=['GET', 'POST'])
def user(user):
    if user not in users:
        return redirect(url_for('index'))
    return render_template('profile.html', user=users[user])

@flask_login.login_required
@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
