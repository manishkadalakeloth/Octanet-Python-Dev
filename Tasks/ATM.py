class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("The deposit amount must be positive.")
            self.balance += amount
            print(f"${amount} has been deposited. Your new balance is: ${self.balance}")
        except ValueError as e:
            print(e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("The withdrawal amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= amount
            print(f"${amount} has been withdrawn. Your new balance is: ${self.balance}")
        except ValueError as e:
            print(e)

    def exit(self):
        print("Thank you for using our ATM. Goodbye!")
        exit()

def atm_menu():
    atm = ATM()
    
    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
            elif choice == 3:
                amount = float(input("Enter the amount to withdraw: "))
                atm.withdraw(amount)
            elif choice == 4:
                atm.exit()
            else:
                print("Invalid option. Please select a valid option from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    atm_menu()
