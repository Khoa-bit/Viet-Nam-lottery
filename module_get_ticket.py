from random import shuffle

digits_bank = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_ticket():
	shuffle(digits_bank)
	ticket = digits_bank[0:6]
	return ticket

# print(get_ticket())