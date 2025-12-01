from flask import render_template, session, redirect, url_for

def get_cart_items(customer_id):
    # TODO: Replace with actual MySQL SELECT query for cart items
    dummy_items = [
        {"name": "Item A", "price": 199.00, "quantity": 1},
        {"name": "Item B", "price": 49.00, "quantity": 2}
    ]
    return dummy_items

def cart_page():
    if "customer_id" not in session:
        return redirect(url_for("customer.login"))

    items = get_cart_items(session["customer_id"])

    total = sum(item["price"] * item["quantity"] for item in items)

    return render_template(
        "customer_cart.html",
        name=session["customer_name"],
        items=items,
        total=total
    )


