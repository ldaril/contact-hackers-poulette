import sqlite3
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # Connect to the Docker container
db = client['hp_db']
collection = db['messages']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html", errors={})

@app.route("/submit-form", methods=["POST"])
def submit_form():    
    errors = {}
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    country = request.form['country']
    gender = request.form.get('gender')
    subject = request.form.getlist('subject')
    message = request.form['message']

    if not first_name:
        errors['first_name'] = 'First name is required.'
    if not last_name:
        errors['last_name'] = 'Last name is required.'
    if not email:
        errors['email'] = 'Email is required.'
    if not country:
        errors['country'] = 'Country is required.'
    if not gender:
        errors['gender'] = 'Gender is required.'
    if not message:
        errors['message'] = 'Message is required.'

    if errors:
        return render_template('contact.html', errors=errors, form=request.form)
    else:
        collection.insert_one({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'country': country,
            'gender': gender, 
            'subject': subject, 
            'message': message
        })
        return render_template("message_sent.html", form=request.form)
