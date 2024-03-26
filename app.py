from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html")

@app.route("/test")
def test():
    return render_template("test.html")

# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3