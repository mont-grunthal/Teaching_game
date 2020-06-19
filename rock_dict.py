#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import sys


# In[ ]:

combos = {("rock", "paper"): "You Win!",
            ("rock", "scissors"): "You Lost!",
            ("paper", "rock"): "You Lost!",
            ("paper", "scissors"): "You Won!",
            ("scissors", "rock"): "You Won!",
            ("scissors", "paper"): "You Lost!"}

options = ["rock","paper","scissors"]

def play(your_choice, combos, options):

    your_choice = your_choice.lower()
    comp_choice = options[np.random.randint(0,3)]
    print(f"The computer chose: {comp_choice}")

    if your_choice == comp_choice:
        print("It's A Tie!")
    else:
        print(combos[(comp_choice,your_choice)])


# In[ ]:


print("Rock, Paper, Scissors... \n")

while True:
    player_choice = input("Input your choice: ")
    play(player_choice,combos,options)
    print(" ")
    quit = input("Play again? y/n: ").lower()
    if quit == "n":
        sys.exit()
    print("")
