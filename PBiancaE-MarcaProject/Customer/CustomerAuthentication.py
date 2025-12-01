import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="emarca_db"
    )

def create_customer_account(name, email, password):
    db = connect_db()
    cursor = db.cursor()

    hashed_pw = generate_password_hash(password)

    query = "INSERT INTO customers (username, password) VALUES (%s, %s)"
    values = (username, hashed_pw)

    cursor.execute(query, values)
    db.commit()

    cursor.close()
    db.close()

def authenticate_customer(username, password):
    db = connect_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM customers WHERE username=%s", (username,))
    customer = cursor.fetchone()

    cursor.close()
    db.close()

    if customer and check_password_hash(customer["password"], password):
        return customer

    return None
