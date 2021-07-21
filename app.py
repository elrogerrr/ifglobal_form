from flask import Flask, redirect,url_for,render_template,flash,request,make_response,session
import forms
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig_ionos, DevelopmentConfig_local, DevelopmentConfig_sqlite
from models import db, User

app = Flask(__name__)
app.config.from_object(DevelopmentConfig_sqlite)
csrf = CSRFProtect()

@app.route('/')
def index():
    titulo = 'Inicio'
    if 'email' in session:
        email = session['email']
        print (email)
    return render_template('index.html', titulo = titulo)

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/registro',methods=['GET','POST'])
def registro():
    titulo = 'Registro'
    registro_form  = forms.RegistroForm(request.form)
    if request.method  == 'POST' and registro_form.validate():
        user = User(registro_form.username.data,
                    registro_form.password.data,
                    registro_form.email.data)
        db.session.add(user)
        db.session.commit()
        success_message = 'Datos almacenados correctamente en base de datos !!!'
        flash(success_message)
        print (registro_form.username.data)
        print (registro_form.email.data)
        print (registro_form.password.data)
    return render_template('registro.html', titulo = titulo, form = registro_form)

@app.route('/login', methods=['GET','POST'])
def login():
    titulo = 'Login'
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        session['email'] = login_form.email.data
        email = login_form.email.data
        success_message = 'Bienvenido {} '.format(email)
        flash(success_message)
    return render_template('login.html', titulo = titulo, form = login_form)

@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
    return redirect( url_for('login') )
   

@app.route('/info', methods=['GET', 'POST'])
def info():
    pass



if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
