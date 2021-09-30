import time
import random
import os

def clear():
    # clears the console
    # used for keeping output clean

    _ = os.system('cls')


def loading():
    # a loading bar animation

    print("\n[", end="")

    for _ in range(0, 25):
        x = random.choice([0.05, 0.07, 0.1 ])
        time.sleep(x)
        print("█", end="", flush=True)

    print("]")


def welcome():
    print(r'''
 ____   __   ____  ____  __ _  ____  ____  ____ 
(  _ \ / _\ / ___)/ ___)(  / )(  __)(  __)(  _ \
 ) __//    \\___ \\___ \ )  (  ) _)  ) _)  ) __/
(__)  \_/\_/(____/(____/(__\_)(____)(____)(__)  
                        .--.
                       /.-. '----------.
                       \'-' .--"--""-"-'
                        '--'
''')