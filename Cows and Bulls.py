import random


def randomnumber():
    return random.randint(1000, 9999)


def checknumber(right, guess):
    right = str(right)
    cow = 0
    bull = 0
    for j in range(0, 4):
        if right[j] == guess[j]:
            cow = cow + 1
        else:
            bull = bull + 1
    print(str(cow) +" cows, " + str(bull) + " bulls")
    if cow == 4:
        print("You have won!")
        return True
    else:
        return False


def playagain():
    j = 0
    while j == 0:
        play = input("Do you want to play again? Y or N")
        if play.lower() == "n":
            return False
        elif play.lower() == "y":
            return True
        else:
            print("Enter Y/y or N/n")


print("Welcome to the Cows and Bulls Game!")
i = 0
correctanswer = False
while i == 0:
    print("Enter a number Between 1000 and 9999:")
    number = randomnumber()
    gotright = False
    while gotright == False:
        try:
            answer = input("")
            innumber = int(answer)
        except:
            print("That's not right. Enter the a number Between 1000 and 9999")
        if innumber > 999:
            if innumber < 10000:
                correctanswer = True
                gotright = checknumber(number, answer)

    if correctanswer == True:
        playag = playagain()
        if playag == False:
            print("\nGoodbye!")
            break