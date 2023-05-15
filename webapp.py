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
    return render_template("menu.html",
                           foodMenu=foodMenu,
                           collection=collection)


@app.route("/customise", methods=['GET', "POST"])
def customise():
    pizza = request.args["pizza"]
    return render_template("customisations.html",
                           sizeOptions=sizeOptions,
                           sauceOptions=sauceOptions,
                           baseOptions=baseOptions,
                           pizzaDetails=foodMenu['toppingOptions'][pizza],
                           pizza=pizza
                           )


@app.route("/cart", methods=["GET", "POST"])
def cart():
    if request.method == "GET":
        return render_template("cart.html", order=session['order'], foodMenu=foodMenu)
    else:
        if 'order' not in session:
            session['order'] = []
        category = request.form['category']
        if category == 'toppingOptions':
            price = foodMenu['toppingOptions'][request.form['pizza']]['price'] + \
                    sizeOptions[request.form['size']] + \
                    baseOptions[request.form['base']] + \
                    sauceOptions[request.form['sauce']]
            session['order'].append([category,
                                     request.form['pizza'],
                                     request.form['size'],
                                     request.form['base'],
                                     request.form['sauce'],
                                     price])
        else:
            item = request.form['item']
            price = foodMenu[category][item]['price']
            session['order'].append([category, item, price])
        session.modified = True
        print(session['order'])
        return redirect(url_for('cart'))


@app.route('/remove/<item>')
def remove(item):
    session['order'].pop(int(item))
    session.modified = True
    return redirect(url_for('cart'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

