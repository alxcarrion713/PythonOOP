class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):	
    	self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -=amount
    def display_user_balance(self,amount):
        self.account_balance= amount
        

Alex=User("Alex Carrion","alxcarrion@gmail.com")
Alex.make_deposit(100)
Alex.make_withdrawal(75)
Alex.account_balance

print(Alex.account_balance)