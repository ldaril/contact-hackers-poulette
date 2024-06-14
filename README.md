# Secure form with Python & Flask

[See the instructions for this project](./project_instructions.md)

## Todo / Writeup

+ [x] Create an app.py
+ [x] Create index.html page
+ [x] Create contact.html page and add contact route to app.py
+ [ ] Create a common layout for both pages
+ [x] In the contact page, create a HTML form
    + [ ] Add some styles so my eyes don't bleed
    + [ ] Better way to add countries
+ [ ] Send data 
+ [ ] Validate form input
+ [ ] Sanitize form input
+ [ ] Implement honeypot anti-spam technique
+ [ ] Display error messages
+ [ ] Add thank you page with summary
+ [ ] Add DB

## Basic structure

We need `app.py`, `requirements.txt` and a `templates/index.html` page.

### `app.py`
This is our server-side code.  

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```

Refs: [Flask docs for 2.2.5](https://flask.palletsprojects.com/en/2.2.x/)  
Concepts: python import fom libraries, class instanciation, decorators...

### Run local server 

```
flask run --debug 
```

We use `--debug` in order to not have to reload server everytime we make a change in the code.

We don't need to precise `--app app.py` if the name of our main file is `app.py`

We're telling the browser that when the url is the homepage (`/`), we display the content of `index.html`.

So let's create an index page.

## Create an index page

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🐔 Hackers Poulette 🐔</title>
    </head>
    <body>
        <h1>We are 🐔 Hackers Poulette 🐔 !</h1>
        <p>Welcome to Hackers Poulette shop</p>
    </body>
</html>
```

## Create a contact page with a form

```html
<form action="/submit-form" method="post">
    <div>
        <label for="first_name">First Name</label>         
        <input name="first_name" type="text" id="first_name" placeholder="First Name" required>

        <label for="last_name">Last Name</label>
        <input type="text" id="last_name" name="last_name" placeholder="Last Name" required>
    </div>
    <div>
        <label for="email">Email</label>
        <input type="email" id="email" name="email" required>
    </div>
    <div>
        <label>Gender</label>
        <label for="male"><input type="radio" id="male" name="gender" value="M" required> Male</label>
        <label for="female">
            <input type="radio" id="female" name="gender" value="F" required> Female
        </label>
        <label for="other">
            <input type="radio" id="other" name="gender" value="O" required> Other
        </label>
        <label for="prefer-not">
            <input type="radio" id="prefer-not" name="gender" value="N" required> Prefer not to say
        </label>
    </div>
    <div>
        <label for="country">Country</label>
        <select id="country" name="country" required>
            <option value="">Select your country</option>
            <option value="us">France</option>
            <option value="ca">Belgique</option>
            <option value="uk">Suisse</option>
            <option value="au">Pays-Bas</option>
            <!-- Add better way to add countries later -->
        </select>
    </div>
    <div>
        <label>Subject</label>
        <label for="repair">
            <input type="checkbox" id="repair" name="subject" value="Repair">
            Repair
        </label>
        <label for="order"><input type="checkbox" id="order" name="subject" value="Order"> Order</label>
        <label for="others"><input type="checkbox" id="others" name="subject" value="Others" checked> Others</label>
    </div>
    <div>
        <label for="message">Message</label>
        <textarea id="message" name="message" required></textarea>
    </div>
    <button type="submit">Submit</button>
</form>
```

## Add route to app.py
```python
@app.route("/contact")
def contact():
    return render_template("contact.html")
```