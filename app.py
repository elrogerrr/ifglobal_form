from re import DEBUG
from flask import Flask, redirect, url_for, render_template, flash, request

app = Flask(__name__)

@app.route('/')
def index():
    titulo = 'Inicio'
    return render_template('index.html', titulo = titulo)

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
