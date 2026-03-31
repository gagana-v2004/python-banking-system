def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("data.txt", "r") as f:
            for line in f:
                u, _, _ = line.strip().split(",")
                if u == username:
                    print("Username already exists")
                    return
    except FileNotFoundError:
        pass

    with open("data.txt", "a") as f:
        f.write(f"{username},{password},0\n")

    print("User registered successfully")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("data.txt", "r") as f:
            users = f.readlines()
    except FileNotFoundError:
        print("No users found. Please register first.")
        return None

    for user in users:
        try:
            u, p, b = user.strip().split(",")
        except ValueError:
            continue   # skip wrong lines

        if u == username and p == password:
            print("Login successful")
            return username

    print("Invalid credentials")
    return None