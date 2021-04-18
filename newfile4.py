def init():
	print ("===========  BUDGET  ========== \n")
	print ("This is your handy expense tracker \n\n")
	
	option = int(input("What would you like to do today?\n\nNew Category[1]:\nDeposit funds[2]:\nWithdraw funds[3]:\nTransfer funds[4]:\nCheck balance[5]:\nExit[6]:  ")
	
		#print("Option not available, try again")
		
	if selectOption == 1:
        self.depositExtraFunds()

    elif selectOption == 2:
        self.withdrawFunds()

    elif selectOption == 3:
        self.transferFunds()

    elif selectOption == 4:
        print ('\n Expenses: \n food: $', '{:.2f}'.format(food), '\n electricity: $', '{:.2f}'.format(electricity), '\n entertainment: $', '{:.2f}'.format(entertainment))
    else:
        print('invalid selection')



		print("Option not available, try again")
		init()