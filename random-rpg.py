#!/usr/bin/env python
"""Author: Bash
    Learning about Pythong via a simple RPG where a user is walking a road to Ravenmore
    The user presses ENTER to advance the game
    Each turn, one of three ecents may happen: enemy, item or nothing
    If an enemy encounter begins, the user may type 'fight' or 'run'
    Item signals that an iten has been found
    Nothing means nothing happens that turn"""




# Standard Library
import random


def main():
    """runtime code"""

    # game init

    inventory = [] #inventory
    health = 10 # health
    items = ['Sword', 'Shield', 'Healing Herbs'] # items that can be found
    enemies = ['Goblin', 'Skeleton', 'Wolf', 'Bandit'] # enemies

    # game starts -- runs by default for 20 turns (loop)
    for turn in range(1, 21):
        print(f'\nTurn {turn}:  You take another step toward Ravenmore')


        # when a turn begins, make a random decision as to what happens: enemy, item, or nothing

        event = random.choice(['nothing', 'item', 'enemy'])

        # check the results of the decision (if, else)

        if event == 'nothing':
            print('\nThe road is quiet. Nothing happens\n')

        elif event == 'item':
            found_item = random.choice(items) # select a random item from inventory
            if found_item == 'Healing Herbs':
                print(f"\nYou found {found_item}! You use them to icrease your HP by +1.\n")
                health += 1 # health = health + 1
            elif found_item not in inventory:
                inventory.append(found_item)
                print(f"\nYou found {found_item}!\n")
            else:
                print(f"\nYou found {found_item}! Unfortunately, you already have one.\n")
        
        # if enemy -- ask user if they want to run or fight

        elif event == 'enemy':
            enemy = random.choice(enemies)  # pick randomly a bad guy
            print(f"\nAn enemy appears: {enemy}\n") # tell user who they are up against
            action = input('\nDo you want to fight or run?:').lower()

            if action == 'fight':
                if 'Sword' in inventory:
                    print(f'\nYou bravely fight the {enemy} and win--thanks to your sword!\n')
                    if random.choice([True, False]): # pick true or false
                        print(f'\nBut you were injured in the fight and take -2 HP\n')
                        health -= 2
                elif 'Shield' in inventory:
                    print(f'\nYou fight bravely, but with only a shield, the {enemy} injured you.')
                    health -= 2
                else:
                    print(f'\nYou fight bravely, but without a sword or shield.  You are injured\n')
                    health -= 3
            elif action == 'run':
                if random.choice([True, False]):
                    print('\nYou manage to escape safely!\n')
                else:
                    print(f'\nThe {enemy} catches up and hurts you as you run\n')
                    health -= 2
            else:
                print(f'\nAs you hesitate, the {enemy} attacks you for -3 HP \n')
                health -= 3

        # display current user stats
        
        if health <= 0:
            print('\nYou have lost all of your health and collapse on the road to Ravenmoor.\n')
            break  # when encountered within a loop, the loop ends

        print(f'\nCurrent health: {health}')
        print(f'\nInventory: {inventory}')

        # ask user to press ENTER to move to next turn
        input(f'\nPress ENTER to move to the next turn\n')


    # game ends with a win at Ravenmoor

    if health > 0:
        print('\nCongratulations! You safely made it to Ravenmoor!\n')
    else:
        print('\nGAME OVER!!!  You did not reach the town of Ravenmoor.\n ')






if __name__ == "__main__":
    main()