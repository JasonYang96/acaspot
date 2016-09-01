import flask_login

class Users(flask_login.UserMixin):
    def __init__(self, user, pw, name=None, email=None, number=None, voice_part=None, sing_exp=None, music_exp=None, year=None, major=None, time_commit=None):
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
        self.authenticated = True

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user

    def __repr__(self):
        return '<User %r>' % (self.user)

class Groups:
    groups = {}

    def __init__(self):
        return;
