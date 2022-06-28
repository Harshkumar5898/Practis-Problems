'''
Author  : Harsh Kumar
Date    : 28 jun 2022
Purpose : A multiplayer guess number game
'''

import random

# Function which runs the main game


def Main_Game(player, guesses, guess):
    global Player_1_Guesses
    global Player_2_Guesses

    print(f"{player} TURN : ")
    while guess != Random_Number:
        try:
            guess = int(input(f"\nEnter your guess between {a} and {b} : "))
        except Exception as e:
            print(f"There is an error [{e}]")
            continue
        else:
            guesses += 1
            if player == "Player 1":
                Player_1_Guesses += 1
            elif player == "Player 2":
                Player_2_Guesses += 1

            if guess == Random_Number:
                print(f"\nYou guess the number in {guesses} times")

            else:
                if guess < Random_Number:
                    print(
                        "\nYour Guess is Less than the original number, Enter a Greater number")
                elif guess > Random_Number:
                    print(
                        "\nYour Guess is Greater than the original number, Enter a smaller number")


try:
    a = int(input("Enter the first number to guess between : "))
    b = int(input("Enter the second number to guess between : "))
except Exception as e:
    print(f"There is an error [{e}]")
else:
    Random_Number = random.randint(a, b)
    Player_1_Guesses = 0
    Player_2_Guesses = 0
    Player_1_guess = None
    Player_2_guess = None

    Main_Game("Player 1", Player_1_Guesses, Player_1_guess)
    Main_Game("Player 2", Player_2_Guesses, Player_2_guess)

# Function decide who wins the game

    if Player_1_Guesses == Player_2_Guesses:
        print(
            f"This game is tie \n Score [{Player_1_Guesses} : {Player_2_Guesses}]")
    elif Player_1_Guesses < Player_2_Guesses:
        print(
            f"Player 1 Wins the game \n Score [{Player_1_Guesses} : {Player_2_Guesses}]")
    elif Player_1_Guesses > Player_2_Guesses:
        print(
            f"Player 2 Wins the game \n Score [{Player_1_Guesses} : {Player_2_Guesses}]")
