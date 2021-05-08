class Budget:
	def __init__(self, category):
		self.category = category
		self.amount = amount
		self.data = list()

#methods
	def balance(self, amount):
		return self.amount


    def credit(self, amount):
        self.amount += deposit
        return self.amount


	def transfer(self, amount, category):
			if self.amount < withdraw_amt
				self.amount -= withdraw_amt
				category.amount += amount
				return category.amount
			else:
				return "Fund balance exceeded"


    def debit(self, amount):
        if self.amount < withdraw_amt
            self.amount -= withdraw_amt
            return self.amount
        else:
            return "Fund balance exceeded"

    
#Example Usage

	def category(self):
		
		clothes = Budget('clothes')
		rent = Budget('house-rent')
		fees = Budget('fees')
		transport = Budget('transport')
		savings = Budget('savings')
		

	def fund_budget(category):
        deposit = int(input("Enter amount you want to deposit:  "))
        category.credit()
        print('Deposit successful')
       
    
    def withdrawal(category):
        withdraw_amt = int(input("How much do you want to withdraw:  "))
        category.debit()
        print('Withdrawal successful')


	def fund_transfer(self, category, amount):
		
		while (True):
			withdraw_amt = int(input("\n How much do you want to transfer?:  "))

			if self.amount < withdraw_amt
				self.amount -= withdraw_amt

				transfer_category = input('Enter the category you want to transfer to:  ')
				category.amount += withdraw_amt
				print("Transfer successful")
				
			else:
				return "Fund balance exceeded"
				
				
