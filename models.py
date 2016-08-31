class Users:
    users = {}
    user_id = 0

    def __init__(self):
        self.user_id = 0

    def add_user(self, name, email, number, voice_part, sing_exp, music_exp, year, major, time_commit):
        self.users[str(self.user_id)] = {
            "name": name,
            "email": email,
            "number": number,
            "voice_part": voice_part,
            "sing_exp": sing_exp,
            "music_exp": music_exp,
            "year": year,
            "major": major,
            "time_commit": time_commit
        }
        self.user_id += 1

    def list_users(self):
        for k, v in self.users.items():
            print(k, v)

class Groups:
    groups = {}

    def __init__(self):
        return;
