

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

# This home() function is executed when the user goes to the home page. The test.html file is displayed to the user
@app.route("/")
def home():
    return render_template("index.html", context="Testing") # This sitring is displayed on the home page

@app.route("/userScore", methods=["POST"])
def userScore():
    return render_template("userScore.html", context="Testing")


if __name__ == '__main__':
    app.run(debug=True)
