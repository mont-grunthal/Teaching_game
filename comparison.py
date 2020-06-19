import time
import numpy as np

combos = {("rock", "paper"): "You Win!",
            ("rock", "scissors"): "You Lost!",
            ("paper", "rock"): "You Lost!",
            ("paper", "scissors"): "You Won!",
            ("scissors", "rock"): "You Won!",
            ("scissors", "paper"): "You Lost!"}

options = ["rock","paper","scissors"]


#dict implementation
#removed user interfaces
def play_dict(combos, options):

    your_choice = options[np.random.randint(0,3)]
    comp_choice = options[np.random.randint(0,3)]

    if your_choice == comp_choice:
        "It's A Tie!"
    else:
        combos[(comp_choice,your_choice)]




#elif implementation
#removed user interfaces
def play_elif():

    options = ["rock","paper","scissors"]
    comp_choice = options[np.random.randint(0,3)]
    your_choice = options[np.random.randint(0,3)]

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





t0 = time.time()
for i in range(1000000):
    play_dict(combos,options)
tf = time .time()
dict_time = (tf-t0)


ti = time.time()
for i in range(10000000):
    play_elif()
t1 = time.time()
elif_time = (t1-ti)

times = elif_time/dict_time

print(f"The hash table implementation ran in {dict_time:.2f} seconds.")
print(f"The elif block implementation ran in {elif_time:.2f} seconds.")
print(f"The hash table implementations was {times} times faster that the elif version")
print("After 10000000 runs.")
