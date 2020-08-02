# Form Based Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

# User Based Imports
from flask_login import current_user
from assets.models import User

class DeleteForm(FlaskForm):
    password = PasswordField('Enter Password:', validators=[DataRequired()])
    submit = SubmitField('CONFIRM DELETE')
    def validate_password(self, field):
        if not current_user.match_password(field.data):
            raise ValidationError('Enter correct password!')

class PassForm(FlaskForm):
    oldPassword = PasswordField('Enter your current password:', validators=[DataRequired()])
    password = PasswordField('New Password:', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm New Password:', validators=[DataRequired()])
    submit = SubmitField('CONFIRM')

    def validate_password(self, field):
        if len(field.data)<6:
            raise ValidationError('New password must be atleast 6-characters long!')

    def validate_oldPassword(self, field):
        if not current_user.match_password(field.data):
            raise ValidationError('Enter correct old/current password!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is Invalid!')
        aln = str(field.data).isalnum()
        lower = str(field.data).islower()
        if not (aln and lower):
            raise ValidationError('username can only consist of digits and lower-case english alphabets!')

    def validate_password(self, field):
        if len(field.data)<6:
            raise ValidationError('password must be atleast 6-characters long!')