'''
@Author:    satyajit 

@Goal:      To implement a number guessing game

@Date:      30th Oct 2026

'''

import random

def generate_random_number():
    return random.randint(1, 100)


def get_input():
    return int(input("Guess the number: "))


def main():
    while True:
        random_number = generate_random_number()
       
        while True:
            guess = get_input()

            if guess < random_number:
                print("Guess is too low")
            elif guess > random_number:
                print("Guess is too high")
            else:
                print("Guessed number is correct")
                break
        
        
        if input("Play again? (y/n): ").lower() != "y":
            break


main()



