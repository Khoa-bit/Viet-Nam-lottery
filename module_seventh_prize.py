class Seventh_prize:
	def __init__(self, one=[1,9,4]):
		# Initialize attributes from parent class and a number
		self.one = one

	def check_for_seventh_prize(self, my_ticket):
		# Slice 3 last numbers of my_ticket then,
		# Compare with the 3 numbers.
		# If succeed, say that the ticket wins and return 'state = "Win"'
		self.my_ticket = my_ticket[-3:]
		if self.my_ticket == self.one:
			state = 'Win'
			print('You have won the 7th prize!')
			return state

# For testing
# my_ticket =[3,2,8,1,9,4]
# sep = Seventh_prize()
# state = sep.check_for_seventh_prize(my_ticket)
# print(state)