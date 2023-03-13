from flask import *
from menu import *

app = Flask("__main__")
app.secret_key = "LKjskejdv9w9er8"


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/menu")
def menu():
    return render_template("menu.html", toppingOptions=toppingOptions)


if __name__ == "__main__":
    app.run(debug=True)

