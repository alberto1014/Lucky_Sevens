###
#Lucky Sevens
###

# Start with $10, every game costs $1 to play.
# Roll two dice.
# If the result is seven, win $5(+$4 overall after the $1 cost).
# The game continuously plays until you run out of money.
# At the end, is tells you how many rounds were played.

import sys
import random
money = 10
round_number = 0

while money > 0:
    round_number +=1
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    print "Money you have: %s" %money
    print "Results of Dice: %s, %s" % (dice_1, dice_2)
    if dice_1 + dice_2 ==7:
        money -=1
        money +=5
        print "You Got 7! Money +5"
    else:
        money -= 1 # money = money - 1
        print "Didn't Roll 7!"
if money ==0:
    print "You Have no more money!"
    print "You've played %s games!" %round_number
    sys.exit(0)
