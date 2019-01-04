class Bank:
    def __init__(self,name,account_number,total_balance):
        self.name = name
        self.account_number = account_number
        self.total_balance = total_balance
        
        

    def deposit(self,amount):
        self.total_balance += amount
        print (self.total_balance)
        

    def withdrawal(self,amount):
        if self.total_balance < amount:
            print ("Not enough money to withdraw.")

        else:
            self.total_balance -= amount
            print (self.total_balance)

        
