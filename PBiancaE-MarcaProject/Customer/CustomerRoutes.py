from flask import request
from . import customer_bp

from .CustomerLogin import login_page
from .CustomerSignUp import signup_page
from .CustomerDashboard import dashboard_page
from .CustomerCart import cart_page      # ← NEW

@customer_bp.route("/customer/login", methods=["GET", "POST"])
def login():
    return login_page()

@customer_bp.route("/customer/signup", methods=["GET", "POST"])
def signup():
    return signup_page()

@customer_bp.route("/customer/dashboard")
def dashboard():
    return dashboard_page()

@customer_bp.route("/customer/cart")
def cart():
    return cart_page()
