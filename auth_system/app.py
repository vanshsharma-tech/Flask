from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(), default="user")
    is_varified = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
<<<<<<< HEAD
=======

>>>>>>> 7007ecfb34dfe3dae4dfeb0dad15e94b9de1980e
    # def __repr__(self):
    #     return f"<User {self.full_name}>"


@app.route("/")
def home():
    return render_template("index.html")

# run only one time, it will create the database and tables if they do not exist.
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
