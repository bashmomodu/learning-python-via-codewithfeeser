#1/usr/bin/env python
"""Author: Bashir
    Writing a python script that reads from a file"""


def main():
    """runtime code"""

    with open("OpenMe.txt", "r") as myfile:
        print( myfile.read() )    # display to the screen all contents of myfile

if __name__ == "__main__":
    main()

    