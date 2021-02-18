from flask import Flask, render_template, url_for
import datetime
import json

app = Flask(__name__)
now = datetime.datetime.now().strftime("%Y")


@app.route("/")
def index():
    return render_template("index.html", now=now)


@app.route("/about")
def about():
    return render_template("about.html", now=now)


@app.route("/certificates")
def certificates():
    return render_template("certificates.html", now=now)


@app.route("/portfolios")
def portfolios():
    return render_template("portfolios.html", now=now)


@app.route("/blogs")
def blogs():
    return render_template("blogs.html", now=now)


if __name__ == "__main__":
    app.run(debug=True)