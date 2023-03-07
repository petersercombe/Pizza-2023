from flask import *

app = Flask("__main__")
app.secret_key = "LKjskejdv9w9er8"

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/profile/<username>")
def profile(username):
    return f"Hello, {username}!"



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

