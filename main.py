from art import *
from replit import clear 
import random as r

    
fail = False
while not fail:
    print(f"{logo}\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 1000")

    attempts = 0
    difficulty = input("Choose difficulty. 'e' for easy and 'h' for hard: ")
    if difficulty == "e":
        attempts = 10
    else:
        attempts = 5
      
    print(f"\nYou have {attempts} attempts.")
    guess = int(input("\nGuess: "))
    
    computer_choice = r.randint(1, 1000)

    while attempts > 0:
        art = [face1, face2, face3, face4, face5, face6]
        ascii = r.choice(art)
        if guess == computer_choice:
            print(shrek)
            print(f"You got it! The answer is {computer_choice}")
        else:
            if guess < computer_choice:
                print(ascii)
                print("Too low!")
                attempts -= 1
                print(f"\nYou have {attempts} attempts.")
            elif guess > computer_choice:
                print(ascii)
                print("Too high!")
                attempts -= 1
                print(f"\nYou have {attempts} attempts.")
        
            stop = False
            while attempts > 0 and not stop:
                stop = True
                guess = int(input("\nGuess again: "))
                
           
            
    if attempts == 0:
        print(ascii)
        print(f"You failed the game!\n The answer is {computer_choice}")
        restart = input("Type 'r' to restart or 'c' to end the game: ").lower()
        if restart == 'c':
            print(over)
            fail = True
        elif restart == 'r':
            clear()
        
    
