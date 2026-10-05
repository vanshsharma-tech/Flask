import sqlite3

from flask import Flask, render_template, request, flash, redirect
from db.contact import create_table

app = Flask(__name__)

app.secret_key = "nahibataunga"
create_table()


@app.route("/")
def home():
    conn = sqlite3.connect("students.db")
    contacts = conn.execute(""" select * from contact """).fetchall()
    conn.close()
    return render_template("./index.html", context=contacts)


@app.route("/about")
def about():
    return render_template("./about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        # print("Post requested")
        full_name = request.form["full_name"].strip()
        email = request.form["email"].strip()
        phone = request.form["phone"].strip()
        msg = request.form["msg"].strip()

        con = sqlite3.connect("students.db")

        if full_name == "":
            flash("Name field can't be Empty", "danger")
            return redirect("/contact")

        if email == "":
            flash("Email field can't be Empty", "danger")
            return redirect("/contact")

        if len(phone) != 10 or not phone.isdigit():
            flash("Phone number must be 10 digits", "danger")
            return redirect("/contact")

        if len(msg) < 10:
            flash("Message should be more than 10 character", "danger")
            return redirect("/contact")

        con.execute(
            """
            INSERT INTO contact (full_name, email, phone, message)
            VALUES (?, ?, ?, ?)
        """,
            (full_name, email, phone, msg),
        )
        con.commit()
        con.close()

        flash("Thank You, Our Team will Contact You", "success")
        return redirect("/contact")

    else:
        print("Get Request")
    return render_template("./contact.html")


@app.route("/edit-contact/<int:id>", methods=["GET", "POST"])
def editContact(id):
    conn = sqlite3.connect("students.db")
    contact = conn.execute("SELECT * FROM contact WHERE id = ?", (id,)).fetchone()
    conn.close()
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["msg"]

        conn = sqlite3.connect("students.db")
        conn.execute(
            """
            UPDATE contact
            SET full_name = ?, email = ?, phone = ?, message = ?
            WHERE id = ?
        """,
            (full_name, email, phone, message, id),
        )
        conn.commit()
        conn.close()

        flash("Contact updated successfully!", "success")
        return redirect("/")
    return render_template("editContact.html", contact=contact)


@app.route("/delete-contact/<int:id>", methods=["POST","GET"])
def deleteContact(id):
    conn = sqlite3.connect("students.db")
    contact = conn.execute("SELECT * FROM contact WHERE id = ?", (id,)).fetchone()
    conn.close()
    print(contact)
    if request.method == "POST":
        conn = sqlite3.connect("students.db")
        conn.execute("DELETE FROM contact WHERE id = ?", (id,))
        conn.commit()
        conn.close()

        flash("Contact deleted successfully!", "success")
        return redirect("/")
    return render_template("deleteContact.html", contact=contact)


if __name__ == "__main__":
    app.run(debug=True)
