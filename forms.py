from wtforms import Form, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class RegistroForm(Form):
    username=StringField('Nombre')
    email=EmailField('Correo Electronico')
    password=PasswordField('Contraseña')
