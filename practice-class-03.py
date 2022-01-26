# PRACTICE IN CLASS 3

import random

# USER CHOOSES A NUMBER BETWEEN 2 AND 12
userInput = int(input("Enter die roll value from 2 to 12: "))

# INFORM USER ERROR IF NUMBER IS BELOW 2 OR ABOVE 12
while userInput <= 1 or userInput >= 13:
    print("ERROR. Enter a number from 2 to 12.")
    userInput = int(input("Enter die roll value from 2 to 12: "))

dieRoll = userInput
turnNumber = 1
result = ""
win = "Player has won!"
loss = "Player has lost!"

# USER'S FIRST TURN
if dieRoll == 2 or dieRoll == 3 or dieRoll == 12:
    result = loss
elif dieRoll == 7 or dieRoll == 11:
    result = win
else:
    pointNumber = dieRoll
    result = "Next turn..."
print("Turn: ", turnNumber)
print("Dice Total: ", dieRoll)
print("Result: ", result)
print()

# IF USER HAS A SECOND TURN
while result != win and result != loss:
    dieRoll = random.randint(2, 12)
    turnNumber += 1
    result = "Next turn..."  
    if dieRoll == 7:
        result = loss
    if dieRoll == pointNumber:
        result = win
    else:
        result = "Next turn..." 
    print("Turn: ", turnNumber)
    print("Dice Total: ", dieRoll)
    print("Result: ", result)
    print()