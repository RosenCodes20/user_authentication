user_credentials = {}


def registration():
    username = input("Enter a username:")
    if username in user_credentials:
        print("Username already exists!")
    if username not in user_credentials:
        password = input("Enter a password:")
        user_credentials[username] = {"Password": password}
        print("You registered successfully.")


def login():
    if user_credentials:
        print("Welcome back!")
        username = input("Enter your username:")
        password = input("Enter your password:")
        if username in user_credentials and user_credentials[username] == {"Password": password}:
            print("You've successfully logged in!")
            print("You can check your profile by entering the number 3!")
        else:
            print("Login failed.Invalid username or password.")
    else:
        print("You are not registered please go and make registration!")


def check_profile():
    if not user_credentials:
        print("You didn't register.Please go and make registration!")
    else:
        for name, details in user_credentials.items():
            print(f"Username: {name}")
            print(f"Password: {details['Password']}")


def logout():
    if user_credentials:
        user_credentials.clear()
        print("You've successfully logged out!")
    else:
        print("Please first go and make registration and log in!")


def search_username():
    if user_credentials:
        print("Hello searching usernames here!")
        found_name = input("Please enter a username to search in here!:")
        if found_name in user_credentials:
            for name, _ in user_credentials.items():
                print(f"We found a username here!")
                print(f"Username: {found_name}")
        else:
            print("We didn't found this name in here sorry, try again.")

    else:
        print("You didn't make a registration please go and make it fast...")


while True:
    print("\n Welcome to the python console login page!")
    print("1. Registration")
    print("2. Login")
    print("3. Check profile")
    print("4. Logout")
    print("5. Search username")
    print("6. Exit")

    choice = int(input("Enter a operation(1, 2, 3, 4, 5):"))

    if choice == 1:
        registration()
    elif choice == 2:
        login()
    elif choice == 3:
        check_profile()
    elif choice == 4:
        logout()
    elif choice == 5:
        search_username()
    elif choice == 6:
        print("Goodbye!!")
        break
    else:
        print("Invalid operation.Please select a number 1, 2, 3, 4!")
