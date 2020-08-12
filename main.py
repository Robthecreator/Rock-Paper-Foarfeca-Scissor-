import random

choices = ["rock", "paper", "foarfeca"]
user = input("Rock, Paper, Foarfeca: ")

computer_choice = random.randint(0, 2)
computer = choices[computer_choice]

# computer = input("Rock, Paper, Foarfeca: ")

print(user.upper() + " vs. " + computer.upper())

if computer == user:
  print("equal")
elif computer == "rock" and user == "foarfeca" or computer == "paper" and user == "rock" or computer == "foarfeca" and user == "paper":
  print("computer won")
elif user == "rock" and computer == "foarfeca" or user == "paper" and computer == "rock" or user == "foarfeca" and computer == "paper":
  print("you won")
