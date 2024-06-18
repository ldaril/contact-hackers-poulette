from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/submit-form", methods=["POST"])
def submit_form():
    return render_template("message_sent.html", form=request.form)