from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome, it is my flask web page! My name is vamsi. pursuing AIDS "

@app.route("/index")
def index():
    return " Welcome to my index page"


if __name__=="__main__":
    app.run(debug=True)






