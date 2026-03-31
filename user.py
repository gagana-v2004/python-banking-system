def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("data.txt", "a") as f:
        f.write(f"{username},{password},0\n")

    print("User registered successfully")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("data.txt", "r") as f:
        users = f.readlines()

    for user in users:
        u, p, b = user.strip().split(",")
        if u == username and p == password:
            print("Login successful")
            return username

    print("Invalid credentials")
    return None