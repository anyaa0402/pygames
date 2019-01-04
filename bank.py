from BankClass import Bank

bank = Bank("California Bank","Account Number 028",0)

print (bank.name)
print (bank.account_number)

#depositing money
bank.deposit(500)


#withdrawing money
bank.withdrawal(200)

