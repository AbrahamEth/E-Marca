import sqlite3

DB_NAME = "emarcadb.db"

def login_customer(username, password):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM customers WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cur.fetchone()
    conn.close()

    if user:
        print(f"\nLogin Successful! Welcome back, {username}.\n")
        return True
    else:
        print("\n❌ Invalid username or password.\n")
        return False

def main():
    print("=== CUSTOMER LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    login_customer(username, password)

if __name__ == "__main__":
    main()
