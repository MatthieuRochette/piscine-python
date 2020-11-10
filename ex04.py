##
## EPITECH PROJECT, 2020
## piscine-python
## File description:
## ex04
##

"""
------------------------------- TO DO ------------------------------------------
Write a program that takes a string (with input()) and prints it, but changes
every letter for the next one in the alphabet.
If you encounter the letter 'z', your program must give out an 'a'.

!!! Your program must be case-sensitive !!!

#Hint: take a look at functions ord() and chr()
--------------------------------------------------------------------------------
"""

#Do your imports here


def ex04():
    s = input("A string: ")
    for c in s:
        if c == "z" or c == "Z":
            print(chr(ord(c) - 25), end="")
        elif c.isalpha():
            print(chr(ord(c) + 1), end="")
        else:
            print(c, end="")
    print()

#Test
if __name__ == "__main__":
    try:
        ex04()
    except Exception as excp:
        print("Your program encountered an error.")
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")