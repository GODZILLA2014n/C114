from flask import Flask

app=Flask(__name__)


@app.route("/")

def first_flask():

    return "This Is My First Flask Program"

@app.route("/flask_2")
def second_flask():
    return "Python is fun!"

app.run(debug=True)