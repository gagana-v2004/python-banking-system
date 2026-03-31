def deposit(username, amount):
    update_balance(username, amount)


def withdraw(username, amount):
    update_balance(username, -amount)


def check_balance(username):
    with open("data.txt", "r") as f:
        for line in f:
            u, p, b = line.strip().split(",")
            if u == username:
                print("Balance:", b)


def update_balance(username, amount):
    lines = []

    with open("data.txt", "r") as f:
        lines = f.readlines()

    with open("data.txt", "w") as f:
        for line in lines:
            u, p, b = line.strip().split(",")
            if u == username:
                b = str(float(b) + amount)
            f.write(f"{u},{p},{b}\n")