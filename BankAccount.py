class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
        return f"Amount deposited: ${amount} new balance: ${self.balance}"
        # rough idea from directions do not keep
        

    def withdraw(self, amount):
        # rough idea from directions do not keep
        if amount > self.balance:
            self.balance -= 10
            return "Insufficient funds."
        self.balance -= amount
        return f"Amount withdrawn: ${amount} new balance: ${self.balance}"

        
    def get_balance(self):
        print(
            "Your balance is: " + str(self.balance)
        )
    
    def add_intrest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_statement(self):
        print(
            self.full_name,
            "Account No.: " + self.account_number,
            "Balance: " + str(self.balance)
        )

#Last left off on instruction number 4      


Account_1 = BankAccount("Mitchell", "03131592" , 400000)
Account_2 = BankAccount("Michael Westen", "20072013", 5000000 )
Account_3 = BankAccount("John Doe", "12345678", 20)

Account_1.print_statement()
print("___________________")
# Account_1.add_intrest()
# Intrest works
# Account_1.print_statement()
Account_1.get_balance()