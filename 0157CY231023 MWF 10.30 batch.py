# Student System
logged_user = ''
logged = False
students_db = {}  # store user data

def register():
    global students_db
    print("\n--- Student Registration ---")
    username = input("Enter Username: ")

    if username in students_db:
        print("⚠️ Username already exists. Try another one.")
        return main()

    password = input("Enter Password: ")
    name = input("Enter Full Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    course = input("Enter Course: ")
    year = input("Enter Year of Study: ")
    roll_no = input("Enter Roll Number: ")

    students_db[username] = {
        "password": password,
        "name": name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone,
        "address": address,
        "course": course,
        "year": year,
        "roll_no": roll_no
    }

    print(f"\n✅ Registration successful for {name}!\n")
    main()


def login():
    global logged_user, logged
    print("\n--- Student Login ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in students_db and students_db[username]["password"] == password:
        logged_user = username
        logged = True
        print(f"\n✅ Login successful! Welcome, {students_db[username]['name']}.\n")
    else:
        print("❌ Invalid username or password.")
    main()


def show_profile():
    global logged_user, logged
    if logged:
        print("\n--- Student Profile ---")
        for key, value in students_db[logged_user].items():
            if key != "password":
                print(f"{key.capitalize()}: {value}")
    else:
        print("⚠️ Please login first.")
    main()


def update_profile():
    global logged_user, logged
    if logged:
        print("\n--- Update Profile ---")
        print("Leave blank to keep current value.\n")
        for key in students_db[logged_user]:
            if key == "password":
                continue
            new_val = input(f"Update {key.capitalize()} ({students_db[logged_user][key]}): ")
            if new_val.strip():
                students_db[logged_user][key] = new_val
        print("\n✅ Profile updated successfully!\n")
    else:
        print("⚠️ Please login first.")
    main()


def logout():
    global logged_user, logged
    if logged:
        print(f"\n👋 Logged out {students_db[logged_user]['name']}.\n")
        logged_user = ''
        logged = False
    else:
        print("⚠️ No user is logged in.")
    main()


def terminate():
    print("\n🚪 Exiting Student System. Goodbye!\n")
    exit()


def main():
    print("\nWelcome in LNCT")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Profile
        4. Update profile
        5. Logout
        6. Main Menu
        7. Exit

            select option 1/2/3/4/5/6/7: ''')

    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        logout()
    elif response == '6':
        main()
    elif response == '7':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
        main()


# Start program
main()
