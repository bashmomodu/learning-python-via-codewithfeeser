#!/usr/bin/env python
"""Author: Bash
    while loops and breaks"""

# Standard Library
import random

def main():
    """runtime code"""

    me_char = ['Frodo', 'Samwise', 'Gandalf', 'Pippen', 'Strider']

    me_choice = ''

    print("Learning about while loopw with conditionals")

    while me_choice != "Gandalf":
        print("As long as Gandalf is not chosen, we continue to loop")
        me_choice = random.choice(me_char)
        print(me_choice)

        print("Learning about while-True")


        while True:  #indefinit
            print("As long as Gandalf is not chosen, we continue to loop\n")
            me_choice = random.choice(me_char)
            print(me_choice, "\n")

            if me_choice == 'Gandalf':
                break #this will escape while or for loop






if __name__ == "__main__":
    main()