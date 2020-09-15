class User:		# declare a class and give it name User
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
    def transfer_money(self,amount,name):
        self.account_balance -=amount   
        self.account_balance +=amount
        return self. account_balance()

Alex= User("David Alex Carrion","alxcarrion@gmail.com")  
Hannah= User("Hannah Carrion","Hcarrion@gmail.com")

# print(Hannah.name)
# Hannah.make_deposit(100)
# print(Hannah.account_balance)

Alex.make_deposit(1000)
Alex.transfer_money(159,Hannah)
print ([Hannah.name],[Hannah.account_balance])



# Alex.make_deposit(100)
# print(Alex.account_balance)
# Alex.make_withdrawal (25)
# print(Alex.account_balance)
# print([Alex.name],[Alex.account_balance])


# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance