# Secure form with Python & Flask

[See the instructions](./project_instructions.md)

## Todo / Writeup

+ [x] Create an app.py
+ [x] Create index.html page
+ [ ] Create contact.html page and add contact route to app.py
+ [ ] Create a common layout for both pages
+ [ ] In the contact page, create a HTML *semantic* form

## `app.py`

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

## Run local server 

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
