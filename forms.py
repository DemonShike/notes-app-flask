from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import InputRequired, Email, Length, Regexp,DataRequired
from email_validator import validate_email, EmailNotValidError




class MyForm(FlaskForm):
    contenido = CKEditorField('contenido')

class RegistrationForm(FlaskForm):
    username = StringField('Username',render_kw={'id':"my-input"} ,validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('Email', render_kw={'placeholder':"Ingresa tu email"},validators=[InputRequired(), Email(message='El campo email no es correcto'), Length(max=50)])
    password = PasswordField('Password', render_kw={'placeholder':"Ingresa tu contraseña"},validators=[InputRequired(), Length(min=8, max=80, message='La contraseña debe tener entre 8 y 80 caracteres'), Regexp( r'^(?=.*[@#$%^&+=!¡])(?=.*[0-9])(?=.*[A-Z])',message='| La contraseña debe contener almenos 1 caracter especial,1 mayuscula y 1 numero')])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    email = StringField('Email',id='my-input',render_kw={'placeholder':"Ingresa tu Email"},validators=[InputRequired(),Email('El email no es correecto')])
    password = PasswordField('Password',render_kw={'placeholder':"Ingresa tu contraseña"},validators=[DataRequired('Debes rellenar el campo contraseña'), Length(min=6)])
    submit = SubmitField('Acceder')