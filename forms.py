from wtforms import Form, StringField, PasswordField, TextField, TextAreaField, HiddenField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from models import User

def length_honeypot(form, field):
    if len(field.data)>0:
        raise validators.ValidationError('Este campo debe estar vacio.!!!')

class RegistroForm(Form):
    username=StringField('Nombre',[
        validators.Length(min=4,max=25, message='Ingrese nombre valido. !'),
        validators.Required()
        ])
    email=EmailField('Correo Electronico',[
        validators.Required(),
        validators.Email(message='Ingrese un Email valido . !')
        ])
    password=PasswordField('Contraseña',[
        validators.Length(min=8,max=25, message='Ingrese contraseña valida. !'),
        validators.Required()
        ])
    acepto=BooleanField('',[validators.Required()])
    honeypot = HiddenField('',[length_honeypot])
    def validate_username(form,field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user is not None:
            raise validators.ValidationError('El username ya se encuentra registrado, favor de considerar otra opción.!!!')

class LoginForm(Form):
    email=EmailField('Correo Electronico',[
        validators.Required(),
        validators.Email(message='Ingrese un Email valido . !')
        ])
    password=PasswordField('Contraseña',[
        validators.Length(min=8,max=25, message='Ingrese contraseña valida. !'),
        validators.Required()
        ])
    honeypot = HiddenField('',[length_honeypot])