#1/usr/bin/env python
"""Author: Bashir
    Learning about conditionals"""

def main():
    """runtime code"""

    sky = "blue" # sky = 'blue'

#check is sky has a string value of blue
    if sky == "blue":
        print("Looks like the sky is blue")

#check if sky exists
    if sky:
        print("Looks like the sky exists")

    sky = 99

#check is sky has a string value of blue
    if sky == "blue":
        print("Looks like the sky is blue")

    sky = "orange"

#test if sky is blue or 99

    if sky == "blue":
        print("Looks like the sky is blue")

    elif sky == 99:
        print("Looks like sky is 99")
    else:
        print("Looks like the sky exists but it is not blue or 99")




if __name__ == "__main__":
    main()