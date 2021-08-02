#WAP to make a number guessing game.

import random as play #importing required module

running = True #making it True to make the game running until the player wants to exit

while running:

    passs = True

    while passs: #checking if the player wants to play game or not
        usrC = input("\nType 'play' to play or 'exit' to exit: ")
        usrChoice = usrC.lower()
        if usrChoice != 'play' and usrChoice != 'exit':
            print('Enter valid command!')
        else:
            passs = False

    if usrChoice == 'play': #if user choose to continue to play the game will start
        print("\nYou will only get 7 chances to guess the number randomly selected by the computer, if you guess the number correctly you will win. You will also get hint so that you can guess it correctly\n")
        number = play.randint(1,51)
        allowance = True
        i = 7
        while allowance:
            if i != 0: #checking if the player has more chances left or not
                guess = int(input("Guess a number between 1 and 50: "))
                if guess < number: #comparing guessed number with the random number to give the player hints.
                    print("\nYour number is LESS than the random number.")
                    i -= 1
                    print("You have only", i, "chance(s) left!\n")
                elif guess > number:
                    print("\nYour number is GREATER than the random number.")
                    i -= 1
                    print("You have only", i, "chance(s) left!\n")
                else: #if the guess number is equal to random number game is stopped and score is set to 1
                    score = 1
                    allowance = False
            else: #if there is no chance left player get score is equal to zero and game is stopped
                score = 0
                allowance = False
        if score == 1: #player win the game if score is 1 else he loses
            print("\nYay! You won the game!")
        else:
            print("\nYou lost the game! Better luck next time.\nThe randomly generated number was", number, '.')
    else: #if the player choose to exit the game the loop will end
        running = False
            

print("\nBye! Come back soon.")