class Fifth_prize:
	def __init__(self, one=[7,3,1,1]):
		# Initialize attributes from parent class and a number
		self.one = one

	def check_for_fifth_prize(self, my_ticket):
		# Slice 4 last numbers of my_ticket then,
		# Compare with the 4 numbers.
		# If succeed, say that the ticket wins and return 'state = "Win"'
		self.my_ticket = my_ticket[-4:]
		if self.my_ticket == self.one:
			state = 'Win'
			print('You have won the 5th prize!')
			return state

# For testing
# my_ticket =[3,3,7,3,1,1]
# fip = Fifth_prize()
# state = fip.check_for_fifth_prize(my_ticket)
# print(state)