import sqlite3

DB_NAME = "emarcadb.db"

def register_customer(username, password):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO customers (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        print("\nRegistration successful! You can now log in.\n")
    except sqlite3.IntegrityError:
        print("\n❌ Username already exists! Please try another.\n")
    finally:
        conn.close()

def main():
    print("=== CUSTOMER SIGN UP ===")
    username = input("Create Username: ").strip()
    password = input("Create Password: ").strip()

    register_customer(username, password)

if __name__ == "__main__":
    main()
