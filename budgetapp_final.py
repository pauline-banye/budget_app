list = {}

class Budget:

    def __init__(self, category, amount, balance):

	    self.category = category
	    self.amount = amount
	    self.balance = balance

    def credit(self, amount, balance):
        self.balance +=  credit.amount
        return self.credit
		
    def debit(self, amount, balance):
        self.balance -= debit.amount
        return 
    
    def balance(self, balance):
        def check_amount(self):
            return self.balance

    def transfer(self, category, amount):
        while (True):
            self.transfer = input("What category do you want to transfer from?:  ")
            transfer_amt = int(input("\n How much do you want to transfer?:  "))
			
            if transfer_amt > self.balance:
                print("\n Account balance exceeded, try again")
                transfer_amt = False
            else:
                transfer_cat = int(input('Enter the account you want to transfer to:  '))
                self.transfer.balance -= transfer_amt
                transfer_cat += transfer_amt
                print("Transfer successful")   
        