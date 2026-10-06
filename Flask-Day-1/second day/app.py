from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = "Vansh Sharma"
    person = {"age": 21, "city": "Delhi", "class": "MCA"}
    context = {"person": person, "name": name}
    return render_template("index.html", context=context)

@app.route("/user/<int:userId>")
def user(userId):
    return f"User id : {userId}"

@app.route("/user/<string:name>")
def profile(name):
    return f"My name is : {name}"

if __name__ == "__main__":
    app.run(debug=True)
