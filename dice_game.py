# Jin Yang 260724904

import random

# takes no inputs, generate two random int between 1 - 6 (inclusive), returns the sum of
# the two int

def dice_roll():
    """ (None) -> Int
    Generates two random int between 1 and 6 (inclusive), returns the sum of the two int
    
    >>> random.seed(8)
    >>> dice_roll()
    6
    >>> dice_roll()
    8
    >>> random.seed(6)
    >>> dice_roll()
    7
    >>> dice_roll()
    2
    """
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    dice = dice_one + dice_two
    return dice

# take an int as input that corresponds to the "point" (number rolled either 4, 5, 6, 8, 9, or 10);
# RETURN an int (either 7 or the "point" itself, depending on which gets rolled first);
# PRINT (on same line) result of all the dice rolls carried out before either a 7 or the "point"

 
def second_stage(point):
    """ (int) -> int
    Takes an int (either 4,5,6,8,9, or 10) as input, returns an int corresponding to either 7 or the input itself.
    Also print (on same line) result of dice rolls carried out before the 7 or the point is rolled.
    
    >>> random.seed(6)
    >>> r = second_stage(9)
    8 9
    >>> r
    9
    >>> random.seed(7)
    >>> r = second_stage(8)
    5 10 2 6 8
    >>> r
    8
    >>> second_stage(2)
    Traceback (most recent call last):
    ValueError: the input should be 4,5,6,8,9, or 10
    """
    # input validation
    if point in [2,3,7,11,12]:
        raise ValueError("the input should be 4,5,6,8,9, or 10")
    
    # iterate through dice_roll(), return 7 or dice_roll itself and print the results before them
    
    point_roll = dice_roll()
    
    while point_roll not in [7, point]:
        print(point_roll, end = ' ')
        point_roll = dice_roll() 
    
    print(point_roll)
    return point_roll

# 2 floats as input, return boolean; 1st input corresponds to money player has, 2nd corresponds to how
# much player wants to bet; ONLY allowed to bet more than $0.0, but NOT more than what they own;
# if allowed to play, RETURN true, otherwise Return false

def can_play(money_own, money_bet):
    """ (float, float) -> bool
    Takes 2 floats as input, returns True if money_own is greater than or equal to money_bet, returns False
    otherwise. Returns False if money_bet is equal to 0.0
    
    >>> can_play(6.35, 6.36)
    False
    >>> can_play(5.00, 0.0)
    False
    >>> can_play(7.00, 2.50)
    True
    """
    
    if money_bet == 0.0:
        return False
    if money_own >= money_bet:
        return True
    else:
        return False

# take 2 floats as input: 1st input corresponds to total amt of money player has,
# 2nd corresponds to how much player decides to bet; assume that the given values are such that the player can play
# RETURN a float which corresponds to amt of money player has left after one round of Craps
# DISPLAY result of the Come-Out Roll (1st roll in a round of Craps), as well as what will happen next
# (7 or 11 win, 2 or 3 or 12 lose, move to second stage with any other number)
# if at the end of second stage a 7 was rolled, DISPLAYS statement saying player has lost, if instead point was
# rolled, DISPLAY statement saying player has won

def pass_line_bet(total_money, bet_money):
    """ (float, float) -> float
    Take two floats as input. Return a float representing amount of money player has left after one round of Craps.
    Display result of 1st roll. If 1st roll is 7 or 11, display win message, return sum of two inputs.
    If 1st roll is 2, 3, or 12, display lose message, return difference of two inputs.
    If any other number move to second stage, if at end of second stage a 7 rolled, display lose message, return
    difference of inputs, if the same number rolled, display win message and return sum of inputs.
    
    >>> random.seed(7)
    >>> m = pass_line_bet(13.00, 5.00)
    A 5 has been rolled. Roll again!
    10 2 6 8 6 3 5
    You win!
    >>> m
    18.0
    >>> random.seed(400)
    >>> m = pass_line_bet(5.45, 5.45)
    A 8 has been rolled. Roll again!
    4 9 8
    You win!
    >>> m
    10.9
    >>> random.seed(15)
    >>> m = pass_line_bet(5.45, 5.45)
    A 3 has been rolled. You lose!
    >>> m
    0.0
    """
    come_out = dice_roll()
    win_money = total_money + bet_money
    lose_money = total_money - bet_money
    
    if come_out in [7,11]:
        print("A", come_out, "has been rolled. You win!\nYou now have", "$"+str(round(win_money, 2)))
        return win_money
    elif come_out in [2,3,12]:
        print("A", come_out, "has been rolled. You lose!\nYou now have", "$"+str(round(lose_money, 2)))
        return lose_money
    else:
        print("A", come_out, "has been rolled. Roll again!")
        if second_stage(come_out) == 7:
            print("You lose!\nYou now have", "$" + str(round(lose_money,2)))
            return lose_money
        else:
            print("You win!\nYou now have", "$" + str(round(win_money,2)))
            return win_money
        
def terminate():
    """ (None) -> bool
    returns false
    """
    return False

# takes no input, returns no value. Retrieves two inputs from user. 1st input = money player has, 2nd input = money
# they want to bet. If user doesn't have enough money to play, DISPLAY message indicating and terminate. Otherwise,
# CALLS pass_line_bet with the appropriate inputs in order to bet. At the end, DISPLAY message indicating how much
# money player has left after their bet. The number representing the money left should only have 2 decimals.

def play():
    """ (None) -> None
    Retrieves two inputs from user. 1st input corresponds to money player has (user_money), 2nd input corresponds
    to money they want to bet (user_bet). If user_money is greater than or equal to user_bet, call pass_line_bet with
    the inputs in order to bet. At the end, display message indicating how much money player has left after their bet.
    The number representing the money left should only have 2 decimals maximum.
    
    >>> random.seed(15)
    >>> play()
    Please enter your money here: 12.25
    How much would you like to bet? 5.0
    A 3 has been rolled. You lose!
    You now have $7.25
    >>> random.seed(200)
    >>> play()
    Please enter your money here: 5.0
    How much would you like to bet? 7.25
    Insufficient funds. You cannot play.
    >>> random.seed(125)
    >>> play()
    Please enter your money here:24.0
    How much would you like to bet?17.0
    A 4 has been rolled. Roll again!
    8 11 5 7
    You lose!
    You now have $7.0
    """
    user_money = float(input("Please enter your money here:"))
    user_bet = float(input("How much would you like to bet?"))
    
    if user_money >= user_bet:
        if user_bet == 0.0:
            print("You must bet more than $0.0")
            terminate()
        else:
            pass_line_bet(user_money, user_bet)
    else:
        print("Insufficient funds. You cannot play.")
        terminate()

    
    
        

