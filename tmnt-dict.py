#!/usr/bin/env python
"""Author: Bashir
    Learning about Python Dictionaries"""


def main():
    """runtime code"""

    tmnt = {}
    print(tmnt) # {}

    tmnt = {"leader":  "leaonardo"}
    print(tmnt)

    tmnt["inventor"] = "donatello"
    print(tmnt)             #{"leader": "leornardo", "inventor": "donatello"}

    # print (tmnt[0]) # this will cause an erro
    print(tmnt["inventor"]) # "donatello"
    print(tmnt["leader"])   # "leonardo"


    tmnt["partydude"] = "shredder"
    print(tmnt)

    tmnt["partydude"] = "michaelangelo"

    #print(tmnt["attitude"]) # this will cause an error
    print(tmnt.get("attitude", None))       # .get() is a dict method
    print(tmnt.get("attitude", "That key is not found in the tmnt dictionary"))
    
    print(tmnt)
    del tmnt["partydude"]    # removes this key: value pair
    print(tmnt)             # {"leader": "leornardo", "inventor": "donatello"}


    print(tmnt.keys())   # print all keys
    print(tmnt.values()) #print all values

if __name__ == "__main__":
        main()

        