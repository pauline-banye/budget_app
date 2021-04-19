class Budget:
	#import data


	def __init__(self, category, amount):
		self.category = category
		self.amount = amount
		self.data = []

	def signout(self):
		print("You have signed out of this budget app.")

	def credit(self):
		self.credit = input("Which budget would you like to fund?:  ")
		try:
			if self.category in self.data:
				return self.category
		except:
			print("\nExpense category does not exist.")

		deposit = int(input("Enter amount you want to deposit:  "))
		self.amount += self.credit(deposit)
		print('You have deposited ' + f'{deposit} into  your account')
		self.data.append([self.category, self.amount])
		return self.amount

	def debit(self):
		self.debit = input("Which budget would you like to withdraw from?:  ")
		try:
			if self.category in self.data:
				return self.category
		except:
			print("\nExpense category does not exist.")

		withdraw = int(input("How much do you want to withdraw:  "))
		self.amount -= self.debit(withdraw)
		print('You have withdrawn ' + f'{withdraw} from  your account')
		self.data.append([self.category, self.amount])
		return self.amount

	def balance(self):
		return self.amount

	def transfer(self):
		transfer_from = input("What category do you want to transfer from?:  ")
		try:
			if self.category in self.data:
				return self.category
		except:
			print("\nExpense category does not exist.")

		while (True):
			transfer_amt = int(input("\n How much do you want to transfer?:  "))

			if transfer_amt > self.amount:
				print("\n Account balance exceeded, try again")
				transfer_amt = False
			else:
				transfer_cat = input('Enter the category you want to transfer to:  ')
				try:
					if self.category in self.data:
						return self.category
				except:
					print("\nExpense category does not exist.")

				self.balance -= transfer_amt
				transfer_cat += transfer_amt
				self.data.append([self.category, self.amount])
				print("Transfer successful")

	def new_category(self):
		print ("===========  NEW CATEGORY  ========== \n")

		input("Enter category name?:   ")
		print("New expense category created!")
		self.data.append(self.category)
		more = input ("Would you like to create another category? Yes [1]  :  No [2]:  ")
		if more == 1:
			self.new_category()
		elif more == 2:
			add_fund = input("Would you like to fund this account now?  Yes [1]  :  No [2]:   ")
			if add_fund == 1:
				self.credit()
			elif add_fund == 2:
				exit()
			else:
				print("invalid option, try again")
		else:
			print("invalid option, try again")


	def category(self, amount):
		print("===========  YOUR EXPENSES  ========== \n")
		self.category = input("Which expense do you want to see?:   ")
		try:
			if self.category in self.data:
				return self.category
		except:
			print("\nExpense category does not exist.")

		option = int(input("Create? [1] or Exit [2]  "))
		if (option == 1):
			self.new_category()
		elif (option == 2):
			self.signout()
		else:
			print("invalid option, try again")

	def init(self):
		print ("=============  BUDGET  ============ \n")
		print ("This is your handy expense tracker")
		print("-----------------------------------")
		try:

			options = int(input(
                '\nWhat would you like to do today?\nNew Category[1]\nDeposit funds[2]\nWithdraw funds[3]\nTransfer funds[4]\nCheck balance[5]\nExit[6]"\n'))
		except:
			print('Invalid input')

			if(options == 1):
				self.new_category()
			elif(options == 2):
				self.credit()
			elif (options == 3):
				self.debit()
			elif (options == 4):
				self.balance()
			elif (options == 5):
				self.transfer()
			elif (options == 6):
				self.signout()
			else:
				print('Invalid input\n')





