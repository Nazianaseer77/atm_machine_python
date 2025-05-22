class ATM:
    def __init__(self): 
      """ Initialize the ATM with a default pin and balance."""
      self.pin = "1234"
      self.balance = 1000.0
      self.is_authenticated = False

    def check_pin(self, input_pin):
        """
        verify the entered pin.
         """
        if input_pin == self.pin:
           self.is_authenticated = True
           print("===========================")
           print("pin verified succesfully.\n")
        else:
          print("Incorrect pin. Access denied.\n")
    def check_balance(self):
        """
       Display the current balance if authenticated.
        """
        if self.is_authenticated:
          print("============================")
          print(f"Current Balance: Rs. {self.balance:.2f}\n")
        else:
          print("Please Enter the correct pin first.\n")
    def deposit(self,amount):
        """
        Deposit the specified amount if authenticated and amount is positive.
        """
        if self.is_authenticated:
          if amount > 0:
              self.balance += amount
              print("===========================")
              print(f"Rs. {amount:.2f} Deposit successfully.")
              print(f" New Balance: Rs.{self.balance:.2f}\n")
          else:
              print("Deposit amount must be positive")
        else:
          print("Please Enter the correct pin first")

    def withdraw(self,amount):
        """
        withdraw the specified amount if authenticated, amount is positive,
        and sufficient balance is available.
        """
        if self.is_authenticated:
          if amount <= 0:
              print("============================")
              print("Withdraw amount must be positive.\n")
          elif amount > self.balance:
              print("Insufficient Balance")
          else:
               self.balance -= amount
               print(f"Rs. {amount:.2f} withdraw successfully.")
               print(f"New Balance: Rs. {self.balance:.2f}\n")
        else:
          ("Please Enter the correct pin first")
    def exit(self):
        """
        Exit the ATM session.
        """
        print(" Thank you for using the ATM. Goodbye!")
        return False
    def menu(self):
        """
        Display the menu and handle user interactions.
        """
        print("======== Wellcome to the ATM ========")
        attempts = 0
        while attempts < 3:
            input_pin = input("Please Enter you 4 digit PIN:")
            if input_pin == self.pin:
               self.is_authenticated = True
               print("PIN verified successfully.\n")
               break
            else:
                attempts += 1
                print(f"Incorrect PIN, Attempts left:  {3 - attempts}\n")
        else:
            print("Too many incorrect attempts Exiting.")
            return
        while True:
             print("=========ATM MENU =========")
             print("1. check Balance")
             print("2. Deposit Money")
             print("3. Withdraw Money")
             print("4. Exit")
             choice = input("Please select an option (1-4): ")
             if choice == "1":
                self.check_balnce()
             elif choice == "2":
                 try:
                    amount = float(input("Enter amount to deposit:\n"))
                    self.deposit(amount)
                 except ValueError:
                    print("Invalid input. please enter a numeric value.\n")
             elif choice == "3":
                try:
                   amount = float(input("Enter amount to withdraw:"))
                   self.withdraw(amount)
                except ValueError:
                    print("Invalid input. please enter a numeric value.\n")
             elif choice == "4":
                if not self.exit():
                    break
             else:
                  print("Invalid selection. please choose avalid option.\n")

if __name__=="__main__":
    atm = ATM()
    atm.menu()
        
