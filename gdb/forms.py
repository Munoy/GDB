from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length

class UserLoginForm(FlaskForm):
    profile_nickname = StringField('사용자이름', validators=[DataRequired(), Length(min=1, max=25)])
    profile_image = StringField('프로필사진', validators=[DataRequired()])
