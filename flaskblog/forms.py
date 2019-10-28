from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
  username=StringField('Username',validators=[DataRequired(),Length(min=4,max=10)])
  email=StringField('Email',validators=[DataRequired(),Email()])
  password=PasswordField('Password',validators=[DataRequired()])
  confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
  submit=SubmitField('Sign Up')

  def validate_username(self,username):

    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('That username is already taken. Choose another username.')

  def validate_email(self,email):

    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('That email is already taken. Choose another email.')

class LoginForm(FlaskForm):
  email=StringField('Email',validators=[DataRequired(),Email()])
  password=PasswordField('Password',validators=[DataRequired()])
  remember=BooleanField('Remember me?')
  submit=SubmitField('Login')


class UpdateAccountForm(FlaskForm):
  username=StringField('Username',validators=[DataRequired(),Length(min=4,max=10)])
  email=StringField('Email',validators=[DataRequired(),Email()])
  picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png','jpeg'])])
  submit=SubmitField('Update Account')

  def validate_username(self,username):

    if username.data != current_user.username:

      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError('That username is already taken. Choose another username.')

  def validate_email(self,email):

    if email.data != current_user.email:

      user = User.query.filter_by(email=email.data).first()
      if user:
        raise ValidationError('That email is already taken. Choose another email.')

class PostForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  content = TextAreaField('content', validators=[DataRequired()])
  submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
  email=StringField('Email',validators=[DataRequired(),Email()])
  submit = SubmitField('Reset Password')


  def validate_email(self,email):

    user = User.query.filter_by(email=email.data).first()
    if user is None:
      raise ValidationError('There is no account with that email.')


class ResetPasswordForm(FlaskForm):
  password=PasswordField('Password',validators=[DataRequired()])
  confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
  submit=SubmitField('Confirm')