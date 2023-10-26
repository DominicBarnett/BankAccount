class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
        return f"Amount deposited: ${amount} new balance: ${'{:,}'.format(self.balance)}"
        

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 10
            return "Insufficient funds. Overdraft fee applied"
        self.balance -= amount
        return f"Amount withdrawn: ${amount} new balance: ${'{:,}'.format(self.balance)}"

        
    def get_balance(self):
        print(f"Your balance is: {'{:,}'.format(self.balance)}")
    
    def add_intrest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_statement(self):
        print(f"""
{self.full_name}
Account No.: ****{self.account_number[4:]}
Balance: ${"{:,}".format(self.balance)}
              """
        )

      


Account_1 = BankAccount("Mitchell", "03131592" , 400000)
Account_2 = BankAccount("Michael Westen", "20072013", 5000000 )
Account_3 = BankAccount("John Doe", "12345678", 20)

Account_1.print_statement()
print("___________________")
# Account_1.add_intrest()
# Intrest works
# print("___________________")
# Account_1.print_statement()
# Balance works
# Account_1.get_balance()
# Account_3.withdraw(10)
# Account_3.get_balance()
# print("___________________")
#withdraw works
# print(Account_3.withdraw(100))
# Account_3.get_balance()
# print(Account_3.withdraw(1))
# print("___________________")
# print(Account_3.deposit(20))
# deposit works
