from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


@make_bold
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/bye")
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run(debug=True)