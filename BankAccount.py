class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        balance += amount 
        return f"Amount deposited: ${amount} new balance: ${balance}"
        # rough idea from directions do not keep
        

    def withdraw(self, amount):
        balance -= amount
        return f"Amount withdrawn: ${amount} new balance: ${balance}"
        # rough idea from directions do not keep
        if amount > balance:
            balance -= 10
            return "Insufficient funds."
        
    def get_balance(self):
        print(
            "Your balance is: " + self.balance
        )
    
    def add_intrest(self):
        interest = self.balance * 0.00083

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