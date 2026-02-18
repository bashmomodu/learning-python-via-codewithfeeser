#!/usr/bin/env python

"""Author: Bash
   Learning about F Strings"""






def main():
    """runtime code"""


    # basic variable insertion
    
    name = "bashmo"
    print(f'Hello there {name}') # fill in {name} with bashmo


    # arithmetic operations

    a = 5
    b = 2
    print(f'The sum of {a} and {b}: {a + b}')

    # floating point formatting

    pi = 3.14159
    print(f'Two digits from pi: {pi:.2f}')  # 3.14

    # string padding

    word = 'dragon'
    print(f'This will always be 10 characters: {word:*>10}')

    # reach into a dict 

    webster = {'name': 'Luna', 'class': 'Wizard'}
    print(f'The name of the character is {webster.get("name")}') # Luna
    print(f'The name of the character is {webster["name"]}')

    # using an expression in an f string
    
    health = 10
    print(f'Player Status: {"Alive" if health > 0 else "Dead"}')

    # f strings for HTP Operations

    token = 'QWERTY' # in production, never put a secret in your code
    print(f'http://rzfeeser.com/service?token={token}')
    














if __name__ == "__main__":
        main()