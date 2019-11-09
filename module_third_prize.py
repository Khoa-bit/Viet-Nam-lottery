class Third_prize:
	# For the third prize there are 2 conditions to win
	def __init__(self, one=[6,9,9,6,2], two=[6,3,9,0,2]):
		# Initialize attributes from parent class and numbers
		self.one = one
		self.two = two

	def check_for_third_prize(self, my_ticket):
		# Slice 5 last numbers of my_ticket then,
		# Compare with the 5 numbers of 2 conditions.
		# If succeed, say that the ticket wins and return 'state = "Win"'
		self.my_ticket = my_ticket[-5:]
		if self.my_ticket == self.one or self.my_ticket == self.two:
			state = 'Win'
			print('You have won the 3nd prize!')
			return state

# For testing
# my_ticket =[3,6,3,9,0,2]
# tp = Third_prize([1,1,1,1,1])
# state = tp.check_for_third_prize(my_ticket)
# print(state)