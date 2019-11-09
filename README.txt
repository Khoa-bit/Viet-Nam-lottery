Achievement Unlocked :3
me Read README.txt
---------------------
Main program is: vietnam_lottery_analysis.py (Everything else are modules)
This program is used to see how hard it is to get a prize in Viet Nam lottery.

How Viet Nam lottery works:
1. There are 6 numbers on a lottery ticket.
2. Check for prizes only by the last numbers.
How namy numbers depends on each prizes:
	- JackPot:   The last 6 numbers, 1 winning condition
	- 1st prize: The last 5 numbers, 1 winning condition
	- 2nd prize: The last 5 numbers, 1 winning condition
	- 3rd prize: The last 5 numbers, 2 winning conditions
	- 4th prize: The last 5 numbers, 7 winning conditions
	- 5th prize: The last 4 numbers, 1 winning condition
	- 6th prize: The last 4 numbers, 3 winning conditions
	- 7th prize: The last 3 numbers, 1 winning condition
	- 8th prize: The last 2 numbers, 1 winning condition

<> The Default winning numbers are based on "Prize Borad.png" 
<> Every set of numbers can be change via adding a list to the "state = ...([number here])" variables
i.g.: Change "jp = mJ.Jackpot()"     to "jp = mJ.Jackpot([1,2,3,4,5,6])" makes 954862 is the Jackpot number.
      Change "p3 = m3.Third_prize()" to "p3 = m3.Third_prize([1,2,3,4,5], [9,8,7,6,5])" 
	makes _12345 and _98765 is the third prize number.

Functionalities:
- Tell you how many tries needed to wins a specific prize 
or any from the full prize board, no blacklist. (Realistic)
- Can be used to check if your own ticket win any prize. (change variable my_ticket = ....... in "while" loop 
to your number. Infinite loop if loses)

Haven't been impletemented:
- An UI.
- semi-jackpot and close-jackpot.
For example: if Jackpot: 999999 then:
	+ semi-jackpot: 299999
	+ close-jackpot: 929999, 992999, 999299, 999929, 999992
- Some calculus or graphs. (like The average percentage of getting a prize of all-time or in 1000 tickets 
or Is lottery profitable?, etc.)

----------
This project took me about 10 hours. It's also is my first projects.
Any helps or comments would be sincercely appreciated.
Credits to "Python Crash Course" book by Eric Matthes, where I got the idead and developed upon it.
:3 meow
BTW! Try to win a JackPot by disabling all other prizes, I haven't got one still. :3
Thank you!
