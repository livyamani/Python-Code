class BankAccount:
    def __init__(self, account_number,account_holder_name, balance, account_type):
        self.account_number = account_number
        self.account_holder_name  = account_holder_name 
        self.balance = balance
        self.account_type = account_type
        self.transaction_history = []
    
    def account_holder_details(self):
        print("Account Number: ",self.account_number)
        print("Account Holder Name: ",self.account_holder_name)
        print("Account Type: ",self.account_type)
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposited Amount : Rs. {amount}")
        print(f"Rs {amount} has been deposited in your account")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal Amount : Rs. {amount}")
            print(f"Rs {amount} has been withdrawal from your account")
            
    def check_balance(self):
        print(f"Current balance is Rs {self.balance}.")

    def view_transaction_history(self):
        print("Transaction History")
        if not self.transaction_history:
            print("No transactions")
        else:
            for transaction in self.transaction_history:
                 print(transaction)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance,"Savings")  # call the superclass constructor
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        self.transaction_history.append(f"Interest added: Rs. {self.balance * self.interest_rate}")
        print(f"Interest of Rs. {self.balance * self.interest_rate} added to your account")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance,"Current")  # call the superclass constructor
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > (self.balance + self.overdraft_limit):
            print("Withdrawal denied. Overdraft limit exceeded.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: Rs {amount}")
            print(f"Rs {amount} has been withdrawn from your account")

    def check_overdraft(self):
        available_overdraft = (0, self.overdraft_limit + self.balance)
        if self.balance < 0:
            print(f"Overdraft used: Rs {self.balance}")
        else:
            print(f"Available overdraft: Rs {self.overdraft_limit}")
        
        

savings_account = SavingsAccount("16430000053288", "XXXXX", 10000.02, 0.001)
savings_account.account_holder_details()
savings_account.deposit(float(input("Enter the deposit amount:")))
savings_account.withdraw(float(input("Enter the withdraw amount:")))
print('        --------          ')
savings_account.add_interest()
savings_account.check_balance()
print("       ----------        ")
savings_account.view_transaction_history()
savings_account.check_balance()
print("--------------------------------------------------------------------------------------------------------------------------------")
current_account = CurrentAccount("16430000053289", "XXXXX", 20000.02, 5000)
current_account.account_holder_details()
current_account.deposit(float(input("Enter the deposit amount:")))
current_account.withdraw(float(input("Enter the withdraw amount:")))
print("       ----------        ")
current_account.check_balance()
print("       ----------        ")
current_account.view_transaction_history()
current_account.check_overdraft()
current_account.check_balance()