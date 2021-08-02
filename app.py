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

@app.route('/insession')
def insession():
    titulo = 'insession'
    if 'email' in session:
        email = session['email']
        print (email)
    return render_template('insession.html', titulo = titulo)

@app.route('/header')
def header():
    return render_template('index_header.html')


@app.before_request
def before_request():
    if 'email' not in session and request.endpoint in ['insession']:
        return redirect (url_for('login'))
    elif 'email' in session and request.endpoint in ['login','registro']:
        return redirect (url_for('insession'))

@app.route('/registro',methods=['GET','POST'])
def registro():
    titulo = 'Registro'
    registro_form  = forms.RegistroForm(request.form)
    if request.method  == 'POST' and registro_form.validate():
        user = User(registro_form.username.data,
                    registro_form.email.data,
                    registro_form.password.data,
                    registro_form.acepto.data)
        db.session.add(user)
        db.session.commit()
        success_message = 'Datos almacenados correctamente en base de datos. !!!'
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
        email=login_form.email.data
        password=login_form.password.data
        user=User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(password):
            session['email']=email
            success_message = 'Bienvenido {} '.format(email)
            flash(success_message)
            return redirect ( url_for('insession') )
        else:
            error_message = 'am so sorry ... no se pudio !!!  '.format(email)
            flash(error_message)
        session['email'] = login_form.email.data
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
