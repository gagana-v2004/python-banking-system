def deposit(username, amount):
    if amount <= 0:
        print("Enter valid amount")
        return

    update_balance(username, amount)
    print("Deposit successful")


def withdraw(username, amount):
    balance = get_balance(username)

    if balance is None:
        print("User not found")
        return

    if amount > balance:
        print("Insufficient balance")
        return

    update_balance(username, -amount)
    print("Withdrawal successful")

def check_balance(username):
    balance = get_balance(username)

    if balance is not None:
        print("Balance:", balance)
    else:
        print("User not found")
        
        
def get_balance(username):
    try:
        with open("data.txt", "r") as f:
            for line in f:
                try:
                    u, p, b = line.strip().split(",")
                except ValueError:
                    continue

                if u == username:
                    return float(b)
    except FileNotFoundError:
        return None

    return None


def update_balance(username, amount):
    lines = []

    try:
        with open("data.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Data file not found")
        return

    with open("data.txt", "w") as f:
        for line in lines:
            try:
                u, p, b = line.strip().split(",")
            except ValueError:
                continue

            if u == username:
                b = str(float(b) + amount)

            f.write(f"{u},{p},{b}\n")