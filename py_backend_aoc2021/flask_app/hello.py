from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/best")
def worst_of_all():
    return "<p>You're the best!</p>"
