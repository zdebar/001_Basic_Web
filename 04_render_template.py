from flask import render_template, Flask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("./day-57-start/index.html")


if __name__ == "__main__":
    app.run(debug=True)
