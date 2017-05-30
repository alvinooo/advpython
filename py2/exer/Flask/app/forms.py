# forms.py - forms
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField 
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired, Required

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    sign_in = SubmitField('Sign In')
    register_me = SubmitField('Register Me')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class CreateBookForm(FlaskForm):
    author = StringField('author', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    category = SelectField('category', 
        choices=[('Fiction','Fiction'), ('Non-Fiction','Non-Fiction'),
            ('Autobiography','Autobiography'), ('Literary Fiction', 
                'Literary Fiction'), ('Western', 'Western'), 
                    ('Classic', 'Classic')]) 
    add_book = SubmitField('Add Book')

class DeleteBookForm(FlaskForm):
    delete_bool = BooleanField()
