from flask import render_template, session, redirect, url_for

def dashboard_page():
    if "customer_id" not in session:
        return redirect(url_for("CustomerLogin"))

    return render_template(
        "CustomerDashboard.html",
        name=session["customer_username"]
    )
