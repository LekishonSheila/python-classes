class Account:
    type = "savings"
    
    def __init__(self, account_number, balance, owner, amount):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.amount = amount
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        self.deposits.append({"amount":amount, "narration":"deposit"})
        print(f"Deposited {amount} into account {self.account_number} and the new balance is {self.balance}.")
    

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.withdrawals.append({"amount":amount, "narration":"withdrawal"})
            print(f"Withdrew {amount} from account {self.account_number} and the new balance is {self.balance}.")
    

    def check_balance(self):
        print(f"The balance of account {self.account_number} is {self.balance}.")


    def print_statement(self):
        for transaction in self.deposits + self.withdrawals:
            print(f"{transaction['narration']} - {transaction['amount']}")    


    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            print("You already have an outstanding loan")

        elif amount <= 100:
            print("The loan amount must be more than 100")

        elif len(self.deposits) < 10:
            print("You must atleast have made 10 deposits before borrowing a loan")   

        elif amount > sum([transaction[amount] for transaction in self.deposits])/3:
            print("Loan must excees 1/3 of total deposits")  

        else:
            self.loan_balance += amount
            print(f"You have successful borrowed {amount}. Your loan balance is {self.loan_balance  }")   



    def repay_loan(self, amount):
            if amount > self.loan_balance:
                self.balance +=(amount - self.loan_balance)
                self.loan_balance = 0
                print(f"Your loan has been repaid, your current balance is {self.balance}")

            else:
                self.loan_balance -= amount
                print(f"Your loan balance is {self.loan_balance}")     


    def transfer(self, amount, destination_account):
        if amount > self.balance:
            print("You have insufficient funds, you can't transfer")
        else:
            self.balance -= amount
            destination_account.deposit(amount)
            print(f"You have transfered {amount} from {self.account_number} to account {destination_account.account_number}")    


account1 = Account("123456", 1000, "Shila Seneiya", 5000)
account2 = Account("789012", 500, "Gift Lekishon", 7650)

account1.deposit(200)
account1.withdraw(100)
account1.print_statement()

account1.borrow_loan(200)
account1.repay_loan(150)
account1.check_balance()

account1.transfer(300, account2)
account1.check_balance()
account2.check_balance()
