from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

def index():
    first_name = "John"
    stuff = "This is <strong>Bold</strong> Text"
    return render_template("index.html", first_name=first_name, stuff=stuff)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)

# custum error page


# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500