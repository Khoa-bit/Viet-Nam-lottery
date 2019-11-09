class Second_prize:
	def __init__(self, one=[0,7,9,1,3]):
		# Initialize attributes from parent class and a number
		self.one = one

	def check_for_second_prize(self, my_ticket):
		# Slice 5 last numbers of my_ticket then,
		# Compare with the 5 numbers.
		# If succeed, say that the ticket wins and return 'state = "Win"'
		self.my_ticket = my_ticket[-5:]
		if self.my_ticket == self.one:
			state = 'Win'
			print('You have won the 2nd prize!')
			return state

# For testing
# my_ticket =[1,0,7,9,1,3]
# sp = Second_prize()
# state = sp.check_for_second_prize(my_ticket)
# print(state)