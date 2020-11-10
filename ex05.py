##
## EPITECH PROJECT, 2020
## piscine-python
## File description:
## ex05
##

"""
------------------------------- TO DO ------------------------------------------
Write a program which does the following things:
    - Ask the user for a number.
    - Ask the user for a second number.
    - Ask the user for an operation. ('+', '-', '*', '/', '%')
    - Finally, display the whole calculation.

You should implement some error handling in your program. (division by zero,
invalid parameter, etc...)

You should try to make your code the cleanest possible. (reusable functions, no
useless variables, separate your code in multiple functions)

You must raise execeptions in your program with the following messages:
    - "Invalid number."
    - "Invalid operator."
    - "Division by zero."
    - "Modulo by zero."

#Hint: input(), raise Exception()

#Exemple 1: Valid arguments

number a:10
number b:20
operation:+
10 + 20 = 30

#Exemple 2: Invalid number

number a:a
Invalid number(s).

#Exemple 3: Invalid operator

number a:10
number b:20
operation:toto
Invalid operator.

#Exemple 4: Division by zero

number a:10
number b:0
operation:/
Division by zero.

--------------------------------------------------------------------------------
"""

def addition(a, b):
    return a + b


def substraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise Exception("Division by zero.")
    return a / b


def modulo(a, b):
    if b == 0:
        raise Exception("Modulo by zero.")
    return a % b


def my_calcul():
    # Setup a dictionary with operations as keys and a function as values.
    available_operation = {
        "+": addition,
        "-": substraction,
        "*": multiplication,
        "/": division,
        "%": modulo
    }

    # We cast the return value of input as an int, if there is an error during the cast, it's an invalid parameter.
    # Else, continue with the program
    try:
        nb_a = int(input("number a:"))
        nb_b = int(input("number b:"))
    except:
        raise Exception("Invalid number.")
    else:
        operation = input("operation:")
        if operation not in available_operation:
            raise Exception("Invalid operator.")
        print("{} {} {} = {}".format(nb_a, operation, nb_b, available_operation[operation](nb_a, nb_b)))


if __name__ == "__main__":
    try:
        my_calcul()
    except Exception as e:
        print(e)