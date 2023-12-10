from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    ola_mundo = 'Olá, mundo!'
    return render_template('index.html', ola_mundo=ola_mundo)