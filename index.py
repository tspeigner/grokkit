from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def hello2():
    return "Hello world!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye, cruel world!"

@app.route("/fbdp")
def fbdp():
    return "Foo Bar Dog Pig!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
