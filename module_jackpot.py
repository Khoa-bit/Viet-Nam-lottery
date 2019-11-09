class Jackpot:
	def __init__(self, one=[8,1,2,1,6,0]):
		# Initialize attributes from parent class and a number
		self.one = one

	def check_for_jackpot(self, my_ticket):
		# Compare with the 6 numbers.
		# If succeed, say that the ticket wins and return 'state = "Win"'
		if my_ticket == self.one:
			state = 'Win'
			print('You have won the JackPot!')
			return state

# For testing
# my_ticket = [8,1,2,1,6,0]
# jp = Jackpot([8,1,2,1,6,0])
# state = jp.check_for_jackpot(my_ticket)
# print(state)