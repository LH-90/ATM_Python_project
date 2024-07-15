from atm import ATM

def main():
    atm = ATM(pin_user=1062, balance_user=1879)
    atm.verify_pin()  # Calls the function to verify PIN

if __name__ == "__main__":
    main()
