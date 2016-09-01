from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(Form):
    user = StringField('user', validators=[DataRequired()])
    pw = StringField('pw', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class ProfileForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    number = StringField('number', validators=[DataRequired()])
    year = StringField('year', validators=[DataRequired()])
    major = StringField('major', validators=[DataRequired()])
    voice_part = StringField('voice_part', validators=[DataRequired()])
    sing_exp = TextAreaField('sing_exp', validators=[DataRequired()])
    music_exp = TextAreaField('music_exp', validators=[DataRequired()])
    time_commit = TextAreaField('time_commit', validators=[DataRequired()])

class RegistrationForm(Form):
    user = StringField('user', validators=[DataRequired()])
    pw = StringField('pw', validators=[DataRequired()])
