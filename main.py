from flask import Flask, render_template, redirect, request
from database import Database

app = Flask(__name__)

@app.route('/')
def homepage():
    posts = Database().get()
    return render_template('homepage.html', posts=posts)

@app.route('/mensagem', methods=('GET', 'POST')) 
def createMessage():
    if request.method == 'POST':
        message = request.form['message']

        if message and len(message) < 100:
            Database().insert(message)
            return redirect("/")
    return render_template('createMessage.html')
