import flask_login

class Users(flask_login.UserMixin):
    users = {}

    def __init__(self):
        pass

    def add_user(self, user, pw, name, email, number, voice_part, sing_exp, music_exp, year, major, time_commit):
        if user in self.users:
            return -1

        self.users[user] = {
            "pw": pw,
            "name": name,
            "email": email,
            "number": number,
            "voice_part": voice_part,
            "sing_exp": sing_exp,
            "music_exp": music_exp,
            "year": year,
            "major": major,
            "time_commit": time_commit,
            "is_active": True,
            "is_anonymous": False,
            "is_authenticated": False
        }
        print self.users[user]["is_active"]
        return self.users[user]

    def list_users(self):
        for k, v in self.users.items():
            print(k, v)

    def user_exists(self, user):
        return user in self.users

    def authenticate_user(user, auth):
        self.users[user]["auth"] = auth

    def get_user(self, user):
        return self.users[user]

class Groups:
    groups = {}

    def __init__(self):
        return;
