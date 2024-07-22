class ATM:

    def __init__(self, pin_user, balance_user):

        self.pin_user = pin_user
        self.balance_user = balance_user
        self.attempts = 0

    # Function to verify PIN
    def verify_pin(self):

        while self.attempts < 3:

            input_pin = int(input("Enter your PIN: "))

            if input_pin == self.pin_user:  # If correct PIN entered by the user
                print("PIN verification successful.")
                self.main_menu()  # The user can have access to the main menu
                return

            else:
                self.attempts += 1  # If incorrect PIN entered by the user
                if self.attempts < 3:
                    print("Invalid PIN. Please try again.")

        else:
            print("Your account has been locked.")  # After 3 incorrect attempts, the account is locked


    # Function to display the main menu with different options for the user
    def main_menu(self):
      
      while True:

        print("Hello, what would you like to do?")
        print("1: Displaying the bank account balance")
        print("2: Withdrawing money")
        print("3: Depositing money")
        print("4: Exiting from the ATM")

        user_option = int(input("Choose an option: (1-4) "))

        if user_option == 1:
            self.display_balance()  # The current balance will be displayed

        elif user_option == 2:
            self.withdraw()  # The user will have to choose a withdraw option

        elif user_option == 3:
            self.deposit()  # The user will have to enter an amount to deposit

        elif user_option == 4:
            print("Thank you for using the ATM")  # The user will leave the ATM
            break

        else:
            print("Invalid option. Please enter a valid number.")
            continue  # Restart the loop

        while True:
            user_input = input("Would you like to perform another operation? (yes/no): ")

            if user_input.lower() == "yes":
                break  # Break this loop and continue with main menu
            elif user_input.lower() == "no":
                print("Thank you for using the ATM")  
                return  # The user will leave the ATM
            else:
                print("Sorry, we couldn't proceed with that input. Please try again.")
                # Restart this loop


    # Function to display the current balance amount
    def display_balance(self):

        print(f"The current balance is: {self.balance_user}£.")
        return self.balance_user

    # Function to display the different possibilities for the user to withdraw money
    def withdraw(self):

        print("How much money would you like to withdraw?")
        print("1: 10£")
        print("2: 20£")
        print("3: 30£")
        print("4: 50£")
        print("5: 80£")
        print("6: 100£")
        print("7: Other amount")

        input_number = int(input("Enter an option: (1-7)"))
        numbers = [1, 2, 3, 4, 5, 6]  # Different options for the user to choose
        amounts = [10, 20, 30, 50, 80, 100]  # Amounts of money which correspond to the options
        numbers_amounts = dict(zip(numbers, amounts))  # Create a dictionary with "numbers: amounts" as a "key: value" pair

        if input_number in numbers:  # If the user has typed a number which is in the numbers list
            amount = numbers_amounts[input_number]
            if amount <= self.balance_user:  # If the current balance is more than the amount the user wants to withdraw
                self.balance_user -= amount  # The withdrawn amount is deducted from the current balance
                print(f"{amount}£ has been withdrawn. The new balance is {self.balance_user}£.")  # Confirms that the amount has been withdrawn and displays the new balance
            else:
                print(f"This amount cannot be withdrawn. You only have {self.balance_user}£ on your account.")  # The amount the user wants to withdraw is more than the current balance
        elif input_number == 7:
            self.withdraw_other_amount()  # Function call to withdraw another amount
        else:
            print("Invalid. Please enter a valid number.")
            self.withdraw()  # The withdraw menu will be displayed if the user enters an invalid number (out of 1-7)


    def withdraw_other_amount(self):

        while True:

            input_amount = int(input("Enter another amount: "))  # The user can type another amount
            if input_amount <= self.balance_user:  # If the current balance is more than the amount the user wants to withdraw
                if input_amount > 0 and input_amount % 10 == 0:  # If the amount the user wants to withdraw is a positive number and a multiple of 10
                    self.balance_user -= input_amount  # The withdrawn amount is deducted from the current balance
                    print(f"{input_amount}£ has been withdrawn. The new balance is {self.balance_user}£.")  # Confirms that the amount has been withdrawn and displays the new balance
                    break
                else:
                    print("This amount cannot be withdrawn. Try another one.")  # If the amount entered by the user is not a multiple of 10 or a negative number
            else:
                print(f"This amount cannot be withdrawn. You have less than {input_amount} on your account.")  # The amount the user wants to withdraw is more than the current balance


    def deposit(self):

        print("How much money would you like to deposit?")
        input_deposit = int(input("Enter an amount: "))
        if input_deposit > 0 and input_deposit % 10 == 0:
            self.balance_user += input_deposit  # Adds the amount of the deposit
            print(f"Thank you, your new balance is {self.balance_user}£.")  # Displays the new balance
        else:
            print("This amount cannot be added to your account.")
