#This is a game practise for Random Guess Game
import random
import os.path
from tkinter import*
from tkinter import filedialog
from idlelib.idle_test.test_warning import running_in_idle

#from pathlib import Path

guessTaken = 0
conversation_list = []

ai_conversation = str("Hello! what is your name?")
print (ai_conversation)
conversation_list.append(ai_conversation)

myName = input()

conversation_list.append(myName)

#GUI Start


main_gui = Tk()
main_gui.geometry('440x450')
main_gui.sourceFolder = ''
def chooseDir():
    main_gui.sourceFolder = filedialog.askdirectory(parent=main_gui, initialdir='/', title='Please select a file location to store the game process data')


b_chooseDir = Button(main_gui, text = 'Choose Folder to store the Game Data', width= 50, height = 20, command = chooseDir)
b_chooseDir.grid(row=0,column=0,sticky=(W, E))

label = Label(main_gui, text="Close this Dialog after you have chosen the file location!", bg="white", fg="black", font="none 12 bold").grid(row=1, column=0, sticky=W)


main_gui.mainloop()


file_path = str(main_gui.sourceFolder)
save_path = file_path

name_of_file = ('Game Process Data Book plays by ' + myName)
        



#check whether file is existed or not
#config = Path(file_path + '/' + name_of_file)

#if os.access(name_of_file, os.F_OK):
    #completeName = os.path.join(save_path, name_of_file + '_latest' +".txt")
    #completeName = os.path.join(save_path, 'testing.txt')

#else:
    #completeName = os.path.join(save_path, name_of_file+".txt")
    #completeName = os.path.join(save_path, 'failing.txt')
completeName = os.path.join(save_path, name_of_file+".txt")
#GUI End

print("Your file location is " + file_path)
number = random.randint(1,50)
ai_conversation = str('Well, ' + myName + ', I am thinking of a number between 1 and 50. You may guess it for 10 times to get the correct answer ^ ^')
print (ai_conversation)
conversation_list.append(ai_conversation)


for guessTaken in range(10):
    ai_conversation = str('Take a guess.')
    print (ai_conversation)
    conversation_list.append(ai_conversation)
    
    guess = int(input())
    conversation_list.append(str(guess))

    
    if guess < number:
        ai_conversation = str('Your guess is too low.')
        print (ai_conversation)
        conversation_list.append(ai_conversation)

    elif guess > number:
        ai_conversation = str('Your guess is too high.')
        print (ai_conversation)
        conversation_list.append(ai_conversation)

    elif guess == number:
        break


if guess == number:
    guessTaken = str(guessTaken +1)
    ai_conversation = str('Good job, '+ myName + '! You guessed my number in '+ guessTaken + ' guesses!')
    print (ai_conversation)
    conversation_list.append(ai_conversation)
    userinput = input('Press any key to close the program...')
    print(userinput)
    
    
    
if guess != number:
    number = str(number)
    ai_conversation = str('Nope. The number I was thinking of was ' + number + '.')
    print (ai_conversation)
    conversation_list.append(ai_conversation)
    userinput = input('Press any key to close the program...')
    print(userinput)
    

file1 = open(completeName, "w")

toFile = '\n'.join(conversation_list)

file1.write(toFile)

file1.close()

