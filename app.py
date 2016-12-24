from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/name")
def name():
  return "Joseph Shepley"

@app.route("/website")
def website():
  return "http://www.josephshepley.com/"


@app.route("/search")
def search():
    return render_template("search.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

