from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html', active='dashboard')

@app.route('/products')
def products():
    # In a real app you'd pull products from a DB and pass them here
    return render_template('products.html', active='products')

@app.route('/orders')
def orders():
    # In a real app you'd pull orders from a DB and pass them here
    return render_template('orders.html', active='orders')

@app.route('/customers')
def customers():
    # In a real app you'd pull customers from a DB and pass them here
    return render_template('customers.html', active='customers')

if __name__ == '__main__':
    app.run(debug=True)
