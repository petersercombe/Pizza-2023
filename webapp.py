from flask import *
from menu import *

app = Flask("__main__")
app.secret_key = "LKjskejdv9w9er8"


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/menu", methods=['GET'])
def menu():
    collection = request.args['collection']
    return render_template("menu.html", toppingOptions=toppingOptions, collection=collection)

@app.route("/customise", methods=['GET', "POST"])
def customise():
    pizza = request.args["pizza"]
    return render_template("customisations.html",
                           sizeOptions=sizeOptions,
                           sauceOptions=sauceOptions,
                           baseOptions=baseOptions,
                           pizzaDetails=toppingOptions[pizza]
                           )

if __name__ == "__main__":
    app.run(debug=True)

