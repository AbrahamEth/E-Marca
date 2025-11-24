import getpass, time, sys

def display_startup():  # usage
    print("*" * 170)
    print("Display Start Up Page")
    print("Starting application... (Located at the bottom left corner.)")
    time.sleep(0.2)
    print("\n")
    print("Loading resources... (Located at the bottom left corner.)")
    time.sleep(0.2)
    print("\n")
    print("Welcome! (Display prompt asking the User if he/she is an Admin or not.)")
    print("*" * 170)

def display_admin_page(username):  # usage
    print("\n(Display the ADMIN PAGE)\n(User: {})\n".format(username))

def display_customer_page():  # usage
    print("\nDisplay the CUSTOMER PAGE directly.\n")

def is_admin_interactive():  # usage
    """Prompt to display Admin Page if the User chooses Yes as Admin."""
    resp = input("Are you an admin? (yes/no): ").strip().lower()
    if resp not in ('yes', 'no'):
        print("\nINVALID RESPONSE! assuming 'no'.")
        return False, None
    if resp == 'no':
        return False, None

    username = input("Admin username: ").strip()

    """We will only use the getpass if we have a real terminal (tty)."""
    if sys.stdin.isatty() and sys.stdout.isatty():
        try:
            pwd = getpass.getpass("Admin password: ")
        except Exception:
            print("\n(getpass failed unexpectedly, fallback to visible input.)")
            print("(getpass not supported here — password will be visible)")
            pwd = input("Admin password: ")
    else:
        print("\nNo TTY (typical for PyCharm Run console). Use visible input.")
        print("(Console not a TTY — entering password will be visible)")
        pwd = input("Admin password: ")

        """For Demo or Practice"""
    if username == "Admin-Bianca" and pwd == "password1":
        print("\nAUTHENTICATION SUCCESSFUL! Welcome {}!\n".format(username))
        return True, username

    elif username == "Admin-Maricar" and pwd == "password2":
        print("\nAUTHENTICATION SUCCESSFUL! Welcome {}!\n".format(username))
        return True, username

    elif username == "Admin-Ethan" and pwd == "password3":
        print("\nAUTHENTICATION SUCCESSFUL! Welcome {}!\n".format(username))
        return True, username

    else:
        print("\nAUTHENTICATION FAILED! Continuing as a Customer.\n")
        return False, None

if __name__ == "__main__":
    display_startup()
    admin, user = is_admin_interactive()
    if admin:
        display_admin_page(user)
    else:
        display_customer_page()
