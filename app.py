# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql
from pymysql.cursors import DictCursor
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

def get_db_connection():
    conf = config.DB_CONFIG.copy()
    # ensure using DictCursor
    conn = pymysql.connect(
        host=conf["host"],
        user=conf["user"],
        password=conf["password"],
        db=conf["db"],
        port=conf["port"],
        charset=conf["charset"],
        cursorclass=DictCursor
    )
    return conn

# ---------- STARTUP PAGE ----------
@app.route('/')
def startup():
    # Display Start Up Page -> choose Admin or Customer
    return render_template('startup.html')

# ---------- CUSTOMER/ADMIN selection routes ----------
@app.route('/customer')
def customer():
    # Display Customer Page (transition: new user? or existing)
    return render_template('customer.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    # Display Sign Up Page (new customers)
    error = None
    if request.method == 'POST':
        username = request.form.get('username','').strip()
        password = request.form.get('password','').strip()
        if not username or not password:
            error = "Please provide username and password."
        else:
            conn = get_db_connection()
            with conn:
                cur = conn.cursor()
                # check existing
                cur.execute("SELECT id FROM customers WHERE username=%s", (username,))
                if cur.fetchone():
                    error = "Username already exists."
                else:
                    cur.execute("INSERT INTO customers (username,password_hash) VALUES (%s,%s)", (username,password))
                    conn.commit()
                    flash("Account created. You can now login.", "success")
                    return redirect(url_for('customer_login'))
    return render_template('signup.html', error=error)

# ---------- CUSTOMER login (enter user & pass) ----------
@app.route('/customer/login', methods=['GET','POST'])
def customer_login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username','').strip()
        password = request.form.get('password','').strip()
        conn = get_db_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM customers WHERE username=%s AND password_hash=%s", (username, password))
            user = cur.fetchone()
            if user:
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['role'] = 'customer'
                return redirect(url_for('customer_dashboard'))
            else:
                error = "Invalid username or password."
    return render_template('customer_login.html', error=error)

# ---------- ADMIN page (enter user & pass) ----------
@app.route('/admin', methods=['GET','POST'])
def admin_page():
    # Display admin login form; if wrong, show e-message
    error = None
    if request.method == 'POST':
        username = request.form.get('username','').strip()
        password = request.form.get('password','').strip()
        conn = get_db_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM admins WHERE username=%s AND password_hash=%s", (username,password))
            admin = cur.fetchone()
            if admin:
                session['user_id'] = admin['id']
                session['username'] = admin['username']
                session['role'] = 'admin'
                return redirect(url_for('admin_dashboard'))
            else:
                error = "Invalid admin credentials. (E-message shown)"
    return render_template('admin.html', error=error)

# ---------- CUSTOMER DASHBOARD ----------
@app.route('/customer/dashboard')
def customer_dashboard():
    if session.get('role') != 'customer':
        flash("Please login as customer.", "warning")
        return redirect(url_for('customer'))
    conn = get_db_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products ORDER BY created_at DESC")
        products = cur.fetchall()
    return render_template('customer_dashboard.html', products=products)

# ---------- ADMIN DASHBOARD (display products, add/update/delete, display customers) ----------
@app.route('/admin/dashboard')
def admin_dashboard():
    if session.get('role') != 'admin':
        flash("Please login as admin.", "warning")
        return redirect(url_for('admin_page'))
    conn = get_db_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products ORDER BY created_at DESC")
        products = cur.fetchall()
        cur.execute("SELECT id, username FROM customers ORDER BY id")
        customers = cur.fetchall()
    return render_template('admin_dashboard.html', products=products, customers=customers)

@app.route('/admin/product/add', methods=['POST'])
def admin_add_product():
    if session.get('role') != 'admin':
        flash("Unauthorized.", "danger")
        return redirect(url_for('admin_page'))
    name = request.form.get('name','').strip()
    price = request.form.get('price','0').strip()
    if name and price:
        conn = get_db_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, float(price)))
            conn.commit()
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/product/delete/<int:product_id>', methods=['POST'])
def admin_delete_product(product_id):
    if session.get('role') != 'admin':
        flash("Unauthorized.", "danger")
        return redirect(url_for('admin_page'))
    conn = get_db_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM products WHERE id=%s", (product_id,))
        conn.commit()
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/product/update/<int:product_id>', methods=['POST'])
def admin_update_product(product_id):
    if session.get('role') != 'admin':
        flash("Unauthorized.", "danger")
        return redirect(url_for('admin_page'))
    name = request.form.get('name','').strip()
    price = request.form.get('price','0').strip()
    if name and price:
        conn = get_db_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("UPDATE products SET name=%s, price=%s WHERE id=%s", (name, float(price), product_id))
            conn.commit()
    return redirect(url_for('admin_dashboard'))

# ---------- Logout ----------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('startup'))

if __name__ == '__main__':
    app.run(debug=True)
