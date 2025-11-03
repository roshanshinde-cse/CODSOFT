# Task-04-RockPaperScissors/rps.py

import random

choices = ["rock", "paper", "scissors"]

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

while True:
    print("\nChoices: rock, paper, scissors")
    user = input("Enter your choice (or 'exit' to quit): ").lower()
    if user == "exit":
        print("Game Over!")
        break
    if user not in choices:
        print("Invalid choice! Try again.")
        continue
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    print(decide_winner(user, computer))
