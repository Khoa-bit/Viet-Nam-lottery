class First_prize:
	def __init__(self, one=[2,8,0,6,7]):
		# Initialize attributes from parent class and a number
		self.one = one

	def check_for_first_prize(self, my_ticket):
		# Slice 5 last numbers of my_ticket then,
		# Compare with the 5 numbers.
		# If succeed, say that the ticket wins and return 'state = "Win"'
		self.my_ticket = my_ticket[-5:]
		if self.my_ticket == self.one:
			state = 'Win'
			print('You have won the 1st prize!')
			return state

# For testing
# my_ticket =[3,2,8,0,6,7]
# fp = First_prize()
# state = fp.check_for_first_prize(my_ticket)
# print(state)