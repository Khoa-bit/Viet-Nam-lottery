class Sixth_prize:
	# For the third prize there are 3 conditions to win
	def __init__(self, one=[6,0,4,1], two=[0,2,1,0], three=[7,7,7,0]):
		# Initialize attributes from parent class and numbers
		self.one = one
		self.two = two
		self.three = three

	def check_for_sixth_prize(self, my_ticket):
		# Slice 4 last numbers of my_ticket then,
		# Compare with the 4 numbers.
		# If succeed, say that the ticket wins and return 'state = "Win"'
		self.my_ticket = my_ticket[-4:]
		if(
			self.my_ticket == self.one
			or self.my_ticket == self.two
			or self.my_ticket == self.three):
			state = 'Win'
			print('You have won the 6th prize!')
			return state

# For testing
# my_ticket =[3,2,6,0,4,1]
# sp = Sixth_prize()
# state = sp.check_for_sixth_prize(my_ticket)
# print(state)