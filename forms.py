from wtforms import Form, StringField, PasswordField, TextField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class RegistroForm(Form):
    username=StringField('Nombre',[
        validators.Length(min=4,max=25, message='Ingrese nombre valido'),
        validators.Required()
        ])
    email=EmailField('Correo Electronico',[
        validators.Required()
        ])
    password=PasswordField('Contraseña',[
        validators.Length(min=8,max=25, message='Ingrese contraseña valida'),
        validators.Required()
        ])
