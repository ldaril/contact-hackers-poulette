from flask import Flask, render_template, request

app = Flask(__name__)


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

    if errors:
        return render_template('contact.html', errors=errors, form=request.form)
    else:
        return render_template("message_sent.html", form=request.form)
