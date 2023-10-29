class Bank:
    def __init__(self):
        self.accounts = {}  
        self.total_balance = 0 
        self.total_loan = 0 
        self.loan_enabled = True  
        self.transaction_history = {} 

    def create_account(self, name, init_balance):
        if name not in self.accounts:
            self.accounts[name] = init_balance
            self.total_balance += init_balance
            self.transaction_history[name] = []
            self.record_transaction(name, f"Account created with an initial balance of {init_balance}")
            print(f"Account for {name} created with an initial balance of {init_balance}")


    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            self.total_balance += amount
            self.record_transaction(name, f"Deposited {amount}")
            print(f"{amount} deposited into {name}'s account.")


    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
                self.total_balance -= amount
                self.record_transaction(name, f"Withdrew {amount}")
                print(f"{amount} withdrawn from {name}'s account.")
            else:
                print("Insufficient balance. Bank is bankrupt.")


    def transfer(self, sender, receiver, amount):
        if sender in self.accounts and receiver in self.accounts:
            if self.accounts[sender] >= amount:
                self.accounts[sender] -= amount
                self.accounts[receiver] += amount
                self.record_transaction(sender, f"Transferred {amount} to {receiver}")
                self.record_transaction(receiver, f"Received {amount} from {sender}")
                print(f"{amount} transferred from {sender} to {receiver}.")
            else:
                print(f"{sender} has insufficient balance to transfer.")


    def check_balance(self, name):
        if name in self.accounts:
            print(f"Available balance for {name}: {self.accounts[name]}")


    def take_loan(self, name):
        if name in self.accounts:
            if self.loan_enabled:
                loan_amount = self.accounts[name] * 2
                self.accounts[name] += loan_amount
                self.total_loan += loan_amount
                self.record_transaction(name, f"Took a loan of {loan_amount}")
                print(f"{name} has taken a loan of {loan_amount}.")
            else:
                print("The loan feature is currently disabled.")


    def check_transaction_history(self, name):
        if name in self.transaction_history:
            print(f"Transaction history for {name}:")
            for transaction in self.transaction_history[name]:
                print(transaction)


    def record_transaction(self, name, description):
        self.transaction_history[name].append(description)

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, init_balance):
        self.bank.create_account(name, init_balance)

    def check_total_balance(self):
        print(f"Total available balance in the bank: {self.bank.total_balance}")

    def check_total_loan(self):
        print(f"Total loan amount in the bank: {self.bank.total_loan}")

    def loan_feature(self, enable):
        self.bank.loan_enabled = enable
        if enable:
            print("Loan feature is now enabled.")
        else:
            print("Loan feature is now disabled.")


my_bank = Bank()
admin = Admin(my_bank)

admin.create_account("abid", 1000)
admin.create_account("shakib", 1500)

abid = "abid"
shakib = "shakib"

abid_balance = my_bank.accounts[abid]
shakib_balance = my_bank.accounts[shakib]

print(f"{abid}'s balance: {abid_balance}")
print(f"{shakib}'s balance: {shakib_balance}")

admin.check_total_balance()
admin.check_total_loan()

admin.loan_feature(True)
abid_loan_amount = abid_balance * 2
my_bank.take_loan(abid)
print(f"{abid}'s balance after taking a loan: {my_bank.accounts[abid]}")
admin.check_total_loan()

shakib_deposit = 500
my_bank.deposit(shakib, shakib_deposit)
print(f"{shakib}'s balance after deposit: {my_bank.accounts[shakib]}")

shakib_withdraw = 2000
my_bank.withdraw(shakib, shakib_withdraw)
print(f"{shakib}'s balance after withdrawal: {my_bank.accounts[shakib]}")

abid_transfer_amount = 800
my_bank.transfer(abid, shakib, abid_transfer_amount)
print(f"{abid}'s balance after transfer: {my_bank.accounts[abid]}")
print(f"{shakib}'s balance after transfer: {my_bank.accounts[shakib]}")


my_bank.record_transaction(abid, "Transaction")
my_bank.check_transaction_history(abid)
