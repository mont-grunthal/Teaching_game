#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import sys


# In[ ]:


def play(your_choice):
    
    your_coice = your_choice.lower()
    options = ["rock","paper","scissors"]
    comp_choice = options[np.random.randint(0,3)]
    
    
    if comp_choice == your_choice:
        out = "It's a Tie!"
        
    elif (comp_choice == "rock") and (your_choice == "paper"):
        out = "You Won!"
    elif (comp_choice == "rock") and (your_choice == "scissors"):
        out = "You Lost!"
    
    elif (comp_choice == "paper") and (your_choice == "rock"):
        out = "You Lost!"
    elif (comp_choice == "paper") and (your_choice == "scissors"):
        out = "You Won!"
        
    elif (comp_choice == "scissors") and (your_choice == "rock"):
        out = "You Won!"
    elif (comp_choice == "scissors") and (your_choice == "paper"):
        out = "You Lost!"
    
    print(f"The computer chose: {comp_choice}")
    print(out)


# In[ ]:


print("Rock, Paper, Scissors... \n")

while True:
    player_choice = input("Input your choice: ")
    play(player_choice)    
    print(" ")
    quit = input("Play again? y/n: ")
    if quit == "n":
        sys.exit()
    print("")

