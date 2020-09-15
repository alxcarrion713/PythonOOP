


class User:
    def __init__(self, nameInput, emailInput):
        self.name = nameInput
        self.email = emailInput
        self.checkingsAccount = BankAccount(0, 0)
        self.savingsAccount = BankAccount(0.05, 0)

    def depositmoney(self, amount, chosen_account):
        if chosen_account == "checkings":
            self.checkingsAccount.deposit(amount)
            print("depositing {amount}")
        elif chosen_account == "savings":
            self.savingsAccount.deposit(amount)
        else:
            print("acccount does not exist")
        return self

    def withdrawmoney(self, amount, chosen_account):
        if chosen_account == "checkings":
            self.checkingsAccount.withdraw(amount)
            print("withdrawing ${amount}")
        if chosen_account == "savings":
            self.savingsAccount.withdraw(amount)
            print("insufficient funds, deducting $5")
        return self

    def displaybalance(self, chosen_account):
        if chosen_account == "checkings":
            self.checkingsAccount.display_account_info()
        elif chosen_account == 'savings':
            self.savingsAccount.display_account_info()
            print("Account blance: ${self.balance}")
        return self

    def transfermoney(self, otheruser, amount):
        print(f"transferring ${amount} from {self.name} to {otheruser.name} ")
        self.account_balance -= amount
        otheruser.account_balance += amount
        return self

# user1 = User("Troy", 'troy@gmail.com')
# user2 = User("Hercules", 'h@gmail.com')
user3 = User("Athena", 'wisdom@gmail.com')
# user4 = User("Hermes", 'messenger@gmail.com')


class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
        return self

    def display_account_info(self):
      

    def yeild_interest(self):
        if self.balance >0:
            self.balance = self.balance + (self.balance * self.interest_rate)
        return self

# account1 = BankAccount(0.05, 0)
# account1.deposit(100).yeild_interest().display_account_info()



user3 = User("Athena",'wisdom@gmail.com')
user3.depositmoney(20, 'checkings').withdrawmoney(5, 'checkings').displaybalance("savings")

print(user3.name)
user3.depositmoney(50, "checkings")
user3.depositmoney(100, "savings")
user3.depositmoney(100, "collegefundFormykids")

user3.checkingsAccount.display_account_info()
user3.savingsAccount.display_account_info()
