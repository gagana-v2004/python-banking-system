from user import register, login
from bank import deposit, withdraw, check_balance

def menu(user):
    while True:
        print("\n1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            deposit(user, float(input("Amount: ")))
        elif choice == "2":
            withdraw(user, float(input("Amount: ")))
        elif choice == "3":
            check_balance(user)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

def main():
    print("1.Register 2.Login")
    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        user = login()
        if user:
            menu(user)

main()