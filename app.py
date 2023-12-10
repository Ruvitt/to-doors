from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    nome = 'Ruan'
    return render_template('index.html', nome = nome)