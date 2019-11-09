import module_get_ticket as mgt
import module_jackpot as mJ
import module_first_prize as m1
import module_second_prize as m2
import module_third_prize as m3
import module_fourth_prize as m4
import module_fifth_prize as m5
import module_sixth_prize as m6
import module_seventh_prize as m7
import module_eighth_prize as m8

# Set up some variables.
my_ticket = []
number_of_tickets = 0
state = ''

# Set up winning conditions.
# Pass arguments for parameters of each module.
# To use default winning conditions, leave each parentheses blank.
jp = mJ.Jackpot()
p1 = m1.First_prize()
p2 = m2.Second_prize()
p3 = m3.Third_prize()
p4 = m4.Fourth_prize()
p5 = m5.Fifth_prize()
p6 = m6.Sixth_prize()
p7 = m7.Seventh_prize()
p8 = m8.Eighth_prize()

# The fun part! :3
# while loop is used to keep pulling numbers until my_ticket wins.
while True:
	# Pull numbers and increment 1 to number_of_tickets.
	# Toggle "print(my_ticket)" function
	# to see or hide the enormous list of tickets.
	my_ticket = mgt.get_ticket()
	number_of_tickets += 1
	print(my_ticket)

	# Test conditions to win and instanly "break" the loop if a ticket wins.
	# Toggle any "state = ..." variable to blacklist that prize.
	# Jackpot?
	state = jp.check_for_jackpot(my_ticket)
	if state == 'Win':
		break
	# 1st prize?
	state = p1.check_for_first_prize(my_ticket)
	if state == 'Win':
		break
	# 2nd prize?
	state = p2.check_for_second_prize(my_ticket)
	if state == 'Win':
		break
	# 3rd prize?	
	state = p3.check_for_third_prize(my_ticket)
	if state == 'Win':
		break
	# 4th prize?	
	state = p4.check_for_fourth_prize(my_ticket)
	if state == 'Win':
		break
	# # 5th prize?
	# state = p5.check_for_fifth_prize(my_ticket)
	# if state == 'Win':
	# 	break
	# # 6th prize?
	# state = p6.check_for_sixth_prize(my_ticket)
	# if state == 'Win':
	# 	break
	# # 7th prize?
	# state = p7.check_for_seventh_prize(my_ticket)
	# if state == 'Win':
	# 	break
	# # 8th prize?
	# state = p8.check_for_eighth_prize(my_ticket)
	# if state == 'Win':
	# 	break


print(f"After {number_of_tickets} tickets.")