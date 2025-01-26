from flask import Flask

app = Flask(__name__)  #It creates an instance of WSGI application

@app.route("/")
def welcome():
    return "Welcome to the first flask code.i am learning flask.This is an edit."

@app.route("/index")
def home():
    return "Hello Everyone, Welcome to the home page of my first flask code."


if __name__ == "__main__":
    app.run(debug=True)