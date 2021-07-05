from flask import Flask, redirect, url_for, render_template, flash, request
import forms

app = Flask(__name__)

@app.route('/')
def index():
    titulo = 'Inicio'
    return render_template('index.html', titulo = titulo)

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/registro', methods=[ 'GET', 'POST' ] )
def registro():
    titulo = 'Registro'
    registro_form  = forms.RegistroForm(request.form)
    if request.method  == 'POST':
        print (registro_form.username.data)
        print (registro_form.email.data)
        print (registro_form.password.data)

    return render_template('registro.html', titulo = titulo, form = registro_form)



if __name__ == '__main__':
    app.run(debug=True)
