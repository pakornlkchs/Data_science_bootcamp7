class Atm:
    def __init__(self, id, bank, location, balance, pin):
        self.id = id
        self.bank = bank
        self.location = location
        self.balance = balance
        self.pin = pin

    def login(self):
        n_try = 0
        while True:
            enter_pin = input(f"Please enter security pin\n")
            if self.pin == int(enter_pin):
                print("Login successfully!")
                break
            elif n_try < 2:
                n_try += 1
                print("Please try again")
            else:
                print("Your account is suspended, Please contact bank staff")
                break
        
    def deposit(self, dep_amount):
        self.balance += dep_amount
        print(f"[{self.id}] deposited {dep_amount} THB\n[{self.id}] current balance is {self.balance} THB")
    
    def withdraw(self, wit_amount):
        if self.balance < wit_amount:
            print(f"id: [{self.id}] doesn't have enough balance to withdraw")
        else:
            self.balance -= wit_amount
            print(f"[{self.id}] withdrew {wit_amount} THB\n[{self.id}] current balance is {self.balance} THB")
    
    def transfer(self, new_id, tf_amount):
        if self.balance < tf_amount:
            print(f"id: [{self.id}] doesn't have enough balance to transfer")
        else:
            self.balance -= tf_amount
            new_id.balance += tf_amount
            print(f"[{self.id}] transfer to [{new_id.id}]: {tf_amount} THB")
            print(f"[{self.id}] balance: {self.balance} THB")
            print(f"[{new_id.id}] balance: {new_id.balance} THB")

    def check_balance(self):
        print(f"[{self.id}] balance is {self.balance} THB") 
        
        
