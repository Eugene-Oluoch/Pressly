#imports
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError
from flask_login import current_user
from app.models import User


#Register Form 
class Register(FlaskForm):
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please choose a different one")
    
    name = StringField("Name", validators=[DataRequired()],render_kw={"placeholder": "Full Name"})
    email = StringField("Email", validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    password = PasswordField("Password", validators=[DataRequired()],render_kw={"placeholder": "**********"})
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')],render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField("Sign Up")
    
    
#Login Form
class Login(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    password = PasswordField("Password", validators=[DataRequired()],render_kw={"placeholder": "**********"})
    submit = SubmitField("Login")
    
    
#Profile Update Form
class UpdateForm(FlaskForm):
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is taken.Please choose a different one")
    
    name = StringField('Name',validators=[DataRequired()], render_kw={"placeholder":"Name"})
    email = StringField('Email',validators=[DataRequired(), Email()], render_kw={"placeholder":"example@example.com"})
    profile_pic = FileField('Update Profile Pic', validators=[FileAllowed(['jpg','png','jpeg']), DataRequired()])
    bio = TextAreaField('Bio',validators=[DataRequired()], render_kw={"placeholder":"Tell us more about yourself"})
    submit = SubmitField('Update')
