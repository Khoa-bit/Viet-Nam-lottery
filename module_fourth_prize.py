class Fourth_prize:
	# For the third prize there are 7 conditions to win
	def __init__(self, one=[5,6,2,4,7], two=[0,0,8,2,9], three=[1,5,2,8,3],
		four=[4,3,0,1,9], five=[1,7,3,3,1], six=[8,9,4,2,2], seven=[2,6,6,7,8]):
		# Initialize attributes from parent class and numbers
		self.one = one
		self.two = two
		self.three = three
		self.four = four
		self.five = five
		self.six = six
		self.seven = seven

	def check_for_fourth_prize(self, my_ticket):
		# Slice 5 last numbers of my_ticket then,
		# Compare with the 5 numbers of 7 conditions.
		# If succeed, say that the ticket wins and return 'state = "Win"'
		self.my_ticket = my_ticket[-5:]
		if(
			self.my_ticket == self.four 
			or self.my_ticket == self.two
			or self.my_ticket == self.three
			or self.my_ticket == self.four
			or self.my_ticket == self.five
			or self.my_ticket == self.six
			or self.my_ticket == self.seven):
			state = 'Win'
			print('You have won the 4th prize!')
			return state

# For testing
# my_ticket =[3,0,0,8,2,9]
# fop = Fourth_prize([1,1,1,1,1])
# state = fop.check_for_fourth_prize(my_ticket)
# print(state)