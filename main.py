
# functions
def getUserInput():
    hand = input("Enter a value 1-5 [1: Rock, 2: Paper, 3: Scissors, 4:Lizard , 5: Spock]")
    return hand

# Mapping
# ---------
# 1 - Rock
# 2 - Paper
# 3 - Scissors
# 4 - Lizard
# 5 - Spock

def generateComputerHand():
    randomNumber = randint( 1, 5)

    if randomNumber == 1:
        return "Rock"
    elif randomNumber == 2:
        return  "Paper"
    elif randomNumber == 3:
        return "Scissors"
    elif randomNumber == 4:
        return "Lizard"
    else:
        return "Spock"

def compareHands( computerValue, userValue):
    pass

# variables
winner = ""


# The game logic:
# ----------------
# 1.) user has to input a random seed to get the random number generator started
from random import seed
from random import randint

seedString = input("Enter a seed number: ")
seedNumber = int( seedString )
seed(seedNumber)

# 2.) select a hand for either rock, paper, sci... spock [5 choices].  user enters that through the keyboard
userValue   = getUserInput()

# 3.) generate a random hand for the computer
computerValue = generateComputerHand()

# 4.) determine who won



def displayWinnersName( winner ):
    pass

def breakTie():
    pass

# test data / test cases
# scenario 1:   User: rock    , computer: paper -> winner: computer
# scenario 2:   User: Lizard  , computer: paper -> winner: user

# edge cases
# edge case 1: user accidently enters something is not rock paper... lizard. Invalid hand
# edge cae  2: too many arugments
# edge case 3: no arguments (user didnt type in anything)
# edge case 4: computer value and user value are the same (no winner)
# edge case 5: if user types in a negative seed value
# edge case 6: maybe too high of a seed number
