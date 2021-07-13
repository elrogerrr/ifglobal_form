from wtforms import Form, StringField, PasswordField, TextField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class RegistroForm(Form):
    username=StringField('Nombre',[validators.Length(min=4,max=10, message='Ingrese nombre valido'), validators.Required()])
    email=EmailField('Correo Electronico')
    password=PasswordField('Contraseña')
