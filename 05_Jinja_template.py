from flask import render_template, Flask
import random

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number)
    # num pak může být použita přímo v html jako python code {{ num }}


@app.route("guess/<name>")
def guess(name):
    return render_template("guess.html", person_name=name, age=63)


if __name__ == "__main__":
    app.run(debug=True)
