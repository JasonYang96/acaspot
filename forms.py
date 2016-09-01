from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    user = StringField('user', validators=[DataRequired()])
    pw = StringField('pw', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
