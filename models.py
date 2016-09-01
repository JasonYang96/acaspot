import flask_login

class Users(flask_login.UserMixin):
    def __init__(self, user, pw, name, email, number, voice_part, sing_exp, music_exp, year, major, time_commit):
        self.user = user
        self.pw = pw
        self.name = name
        self.email = email
        self.number = number
        self.voice_part = voice_part
        self.sing_exp = sing_exp
        self.music_exp = music_exp
        self.year = year
        self.major = major
        self.time_commit = time_commit
        self.authenticated = False

    def is_active(self):
        return True

    def get_id(self):
        return self.user

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def authenticate_user(self, auth):
        self.authenticated = auth

class Groups:
    groups = {}

    def __init__(self):
        return;
