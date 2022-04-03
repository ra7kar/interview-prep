from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/bye")
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
