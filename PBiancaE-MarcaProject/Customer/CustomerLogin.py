from flask import render_template, request, redirect, url_for, flash, session
from .CustomerAuthentication import authenticate_customer

def login_page():
    if request.method == "POST":
        username = request.form["Username: "]
        password = request.form["Password: "]

        customer = authenticate_customer(username, password)

        if customer:
            session["customer_id"] = customer["id"]
            session["customer_name"] = customer["username"]
            return redirect(url_for("CustomerDashboard"))

        flash("Invalid email or password.", "danger")

    return render_template("CustomerLogin.html")
