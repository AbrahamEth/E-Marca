from flask import render_template, request, redirect, url_for, flash, session
from .CustomerAuthentication import create_customer_account

def signup_page():
    if request.method == "POST":
        username = request.form["Username: "]
        password = request.form["Password: "]

        create_customer_account(username, password)
        flash("Account created successfully!", "success")

        return redirect(url_for("CustomerLogin"))

    return render_template("CustomerSignUp.html")
