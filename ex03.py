##
## EPITECH PROJECT, 2020
## piscine-python
## File description:
## ex03
##

"""
------------------------------- TO DO ------------------------------------------

Write a program that prints the arguments given in the command line, separated
by a space, including the name of the Python file.

It shall print a new line when all the arguments have been printed.

!!! There should not be spaces before the first of after the last argument !!!

!!! You must not print the arguments as a list (there musn't be square braces
in the output unless they are given as arguments) !!!

Hint: import sys

Bonus : Try to do it in only one line of code !
--------------------------------------------------------------------------------
"""

#Do your imports hereunder
from sys import argv as av

def print_args():
    print(*av, sep=" ")

#Tests
if __name__ == "__main__":
    try:
        print_args()
    except Exception as excp:
        print("Your program encountered an error.")
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")