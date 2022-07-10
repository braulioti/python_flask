from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")
