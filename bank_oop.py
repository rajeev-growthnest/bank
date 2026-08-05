class BankAccount :
    def __init__(self,account_holder,account_number,balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance  $: {self.balance}")
        print("-" * 30)

    def deposit(self,amount):
        self.amount = amount
        if self.amount > 0:
           print(f"$ {self.amount} deposited successfully.")
           self.balance += self.amount
        else:
            print("Invalid deposit amount.")   

    def withdraw(self , amount , ):
        self.amount = amount
        if self.amount > 0 and self.amount <= self.balance:
            print(f'$ {self.amount} withdrawal successfully.')
            self.balance -= self.amount

        elif self.amount < 0 :
            print("Invalid withdrawal amount.")  
            
        else:
            print("Insufficient balance.")    

    def check_balance(self):
        print(f"Current Balance $: {self.balance}")


account = BankAccount("Rajeev", 12345678, 1000)

account.deposit(500)

account.display_info()
account.withdraw(700)
account.withdraw(800)
account.check_balance()


