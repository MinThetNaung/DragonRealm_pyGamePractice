import random #to generate a random number
import time #to get time function

def displayIntro():
    print('''You are in a land full of dragons. In front of you, you see two caves.
    In one cave, the dragon is friendly and will share his treasure with you. 
    The other dragon nis greedy and hungry, and will eat you on sight.\n''')
    

def chooseCave():
    Cave = ''
    while Cave != '1' and Cave != '2':
        print("Which cave will you go into? (1 or 2)")
        Cave = input()

    return Cave

def checkCave(chooseCave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(2)


    friendlyCave = random.randint(1, 2)

    if chooseCave == str(friendlyCave):
        print("Give you his treasure!")

    else:
        print("Gobbles you down in one bite!")


playAgain = 'Yes'
while playAgain == 'Yes' or playAgain =='yes' or playAgain =='y':

    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Do you want to play again? (yes or no)")
    playAgain = input()

    

