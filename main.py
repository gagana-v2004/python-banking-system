from user import register, login
from bank import deposit, withdraw, check_balance

print("=== Welcome to Banking System ===")

def menu(user):
    while True:
        print("\n1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
        choice = input("Enter choice: ")

        if choice in ["1", "2"]:
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount")
                continue

        if choice == "1":
            deposit(user, amount)

        elif choice == "2":
            withdraw(user, amount)

        elif choice == "3":
            check_balance(user)

        elif choice == "4":
            break

        else:
            print("Invalid choice")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()
            if user:
                menu(user)

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()