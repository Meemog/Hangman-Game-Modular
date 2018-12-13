import random

def Display_Menu():
    print("""Hello and welcome to hangman. Choose an option:
    1: Play against the computer
    2: Play against another player
    """)

def Get_Choice():

    choice = "0"

    while choice != "1" and choice != "2":
        choice = input("Please enter either '1' or '2'")

    return(choice)

def Get_Word():
    check = False
    while check == False:
        word = input("Choose a word")

        if word.isalpha():
            check = True
        else:
            print("Please only enter a-z charactars")

    word = word.lower()
    return(word)

def Choose_Word(words):
    word = words[random.randint(0,len(words)-1)]
    return word

def Make_Blanks(word):
    blank = []

    for i in range(len(word)):
        blank.append("*")
    blank = "".join(blank)

    return blank

def Get_Letter(used_letters):
    check = False
    while check == False:
        letter = input("Enter a letter")
        if letter.isalpha():
            if len(letter) == 1:
                if letter not in used_letters:
                    check = True
                else:
                    print("Letter in use")
            else:
                print("Letter must be one letter")
        else:
            print("Letter must be a letter")

    letter = letter.lower()

    used_letters.append(letter)

    print("The letters you have used are " + str(used_letters) + "\n")

    return letter, used_letters

def Check_Letter(letter, word, mask, numlives):
    mask = list(mask)
    wordList = list(word)
    Check = False

    for i in range(len(word)):
        if wordList[i] == letter:
            mask[i] = letter
            Check = True
    if Check == False:
        numlives -= 1

    mask = "".join(mask)
    return mask, numlives

def Display_Man(Lives):
    if Lives == 0:
        print("             ")
        print("__________   ")
        print("|/        |  ")
        print("|         0  ")
        print("|        /|\ ")
        print("|        / \ ")
        print("|            ")
        print("|____________")

    if Lives == 1:
        print("             ")
        print("__________   ")
        print("|/        |  ")
        print("|         0  ")
        print("|        /|\ ")
        print("|            ")
        print("|            ")
        print("|____________")

    if Lives == 2:
        print("             ")
        print("__________   ")
        print("|/        |  ")
        print("|         0  ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|____________")

    if Lives == 3:
        print("             ")
        print("__________   ")
        print("|/           ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|____________")

    if Lives == 4:
        print("             ")
        print("             ")
        print("|/           ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|____________")

    if Lives == 5:
        print("             ")
        print("             ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|____________")

    if Num_Lives == 6:
        print("             ")
        print("             ")
        print("            ")
        print("            ")
        print("            ")
        print("            ")
        print("            ")
        print("____________")

    if Lives == 7:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

    return ""

#main

Display_Menu()
words = ["computer", "binary", "mouse", "monitor"]

Choice = Get_Choice()

if Choice == "1":
    word = Choose_Word(words)

elif Choice == "2":
    word = Get_Word()

blanks = Make_Blanks(word)

Used_Letters = []
Num_Lives = 7
running = True

#main loop

while running == True:

    letter, Used_Letters = Get_Letter(Used_Letters)

    blanks, Num_Lives = Check_Letter(letter, word, blanks, Num_Lives)

    print(Display_Man(Num_Lives))
    print(blanks)

    if Num_Lives == 0:
        print("You lose, The word was " + word)
        running = False

    if blanks == word:
        print("You win, The word was " + word)
        running = False




