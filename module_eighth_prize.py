class Eighth_prize:
	def __init__(self, one=[8,2]):
		# Initialize attributes from parent class and a number
		self.one = one

	def check_for_eighth_prize(self, my_ticket):
		# Slice 2 last numbers of my_ticket then,
		# Compare with the 2 numbers.
		# If succeed, say that the ticket wins and return 'state = "Win"'
		self.my_ticket = my_ticket[-2:]
		if self.my_ticket == self.one:
			state = 'Win'
			print('You have won the 8th prize!')
			return state

# For testing
# my_ticket =[3,2,8,0,8,2]
# ep = Eighth_prize()
# state = ep.check_for_eighth_prize(my_ticket)
# print(state)