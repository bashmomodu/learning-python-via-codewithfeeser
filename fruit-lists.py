#!/usr/bin/env python
"""Author: Bashir
    All about lists"""


def main():
    """runtime code"""

    #            0.         1.        2.  
    fruit = ["strawberry", "lime", "lemon"] # 3 items
    print(fruit)
    print(fruit[0])         # "strawberry"
    print(fruit[2])         # "lemon"
    print(fruit[-1])        # "lemon"
    print(fruit[-2])        # "lime"
    fruit.append("apple")   # "strawberry", "lime", "lemon", "apple"
    print(fruit)
    print(fruit[-1])

    veggies = ["carrots", "beets"]
    print(veggies)

    fruit.extend(veggies)
    print(fruit)


if __name__ == "__main__":
        main()

        