

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

# This home() function is executed when the user goes to the home page. The test.html file is displayed to the user
@app.route("/")
def home():
    return render_template("test.html", context="Testing") # This sitring is displayed on the home page

# Here, when the user navigates to home/thisCanBeAnything, this finction renders test.html with the arguments of "name", and "r"
@app.route("/<name>")
def admin(name):
    return render_template(".html", var1=name, r=77)

@app.route("/bowser")
def bowser():
    return render_template("base.html")

# This example runs python in the html page
# To see this: navigate to http://HOST:PORT/inline
@app.route("/inline")
def inline():
    return render_template("inline.html", content=["tim", "joe", "bob"])




if __name__ == '__main__':
    app.run(debug=True)
