##
## EPITECH PROJECT, 2020
## piscine-python
## File description:
## ex06
##

"""
------------------------------- TO DO ------------------------------------------
Write a program that:
    - opens a file (test.txt, at the root of the repository),
    - counts the number of vowels in the file (list of vowels: "aeiouy")
    - prints every line containing "42"

Hint: Take a look at the keyword 'with' !

Bonus: count separately each vowel
--------------------------------------------------------------------------------
"""

def ex06():
    # Create a dictionnary that holds the number of occurences for each vowel
    vowel_count = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0,
        "y": 0,
        "Total": 0
    }

    with open("test.txt", "r") as file: # This is a good way to open a file.
        for line in file.readlines(): # for each line of a file...
            if "42" in line:
                print(line, end="")
            for i in line: # for each character of a line...
                try:
                    vowel_count[i] += 1
                except KeyError:
                    pass # ignore the error if the character is not a vowel
                except Exception:
                    exit(84) # do not ignore other (unknown) errors
    print()

    for item in vowel_count.items():
        if item[0] != "Total":
            vowel_count["Total"] += item[1]

    for key, value in vowel_count.items():
        print("{}: {}".format(key, value))


#Test
if __name__ == "__main__":
    try:
        ex06()
    except Exception as excp:
        print("Your program encountered an error.")
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")