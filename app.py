from flask import Flask, redirect, url_for, render_template, flash, request
import forms
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'm1y2s3e4c5r6e7t8k9e0y'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    titulo = 'Inicio'
    return render_template('index.html', titulo = titulo)

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/registro',methods=['GET','POST'])
def registro():
    titulo = 'Registro'
    registro_form  = forms.RegistroForm(request.form)
    if request.method  == 'POST' and registro_form.validate():
        print (registro_form.username.data)
        print (registro_form.email.data)
        print (registro_form.password.data)
    return render_template('registro.html', titulo = titulo, form = registro_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass

@app.route('/info', methods=['GET', 'POST'])
def info():
    pass



if __name__ == '__main__':
    app.run(debug=True)
