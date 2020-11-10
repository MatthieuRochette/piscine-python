##
## EPITECH PROJECT, 2020
## piscine-python
## File description:
## ex07
##

"""
------------------------------- TO DO ------------------------------------------

Let's create Olaf from League of Legends !

We will implement some quotes from this website:
https://leagueoflegends.fandom.com/wiki/Olaf/Quotes

Olaf is a Warrior, let's create a class Warrior which respect the following things:

- A constructor with two parameters: name and weapon.
In the constructor, the warrior say "Leave nothing behind !".

- The instance attributes name and weapon.

- A destructor which display "I'm going.".

- When you print a warrior or use the method "talk", it should print:
"name": I've got my "weapon's name".

- A static method "move" which print:
"name": "random Olaf moving quotes"

- A static method "taunt" which print:
"name": "Olaf taunt quotes"

- A static method "joke" which print:
"name": "Olaf joke quote"

- A static method "attack" which print:
"name": "random Olaf attack quotes"

#Hints: import random

#Outputs example:
Olaf: Leave nothing behind !
Olaf: I've got my Axe
Olaf: I've got my Axe
Olaf: The worth of a man can be measured by the length of his beard, and the girth of his belt buckle.
Olaf: C'mon, I won't hurt you. I promise !
Olaf: Urge to kill, rising !
Olaf: The might of Lokfar approaches !
Olaf: My axe is thirsty.
Olaf: Faster to battle !
Olaf: I'm going.
Congratulation !

--------------------------------------------------------------------------------
"""

import random

move_quotes = [
    "The might of Lokfar approaches !",
    "To plunder !",
    "To action !",
    "I'm going.",
    "Urge to kill, rising !"
]

taunt_quote = "C'mon, I won't hurt you. I promise !"

joke_quote = "The worth of a man can be measured by the length of his beard, and the girth of his belt buckle."

attack_quotes = [
    "Faster to battle !",
    "Chop chop !",
    "My axe is thirsty.",
    "Finally, some fun !",
    "Death by steel !",
    "Obliteration !"
]


class Warrior():
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        print("{}: Leave nothing behind !".format(self.name))

    def __del__(self):
        print("{}: I'm going.".format(self.name))

    def __repr__(self):
        return "{}: I've got my {}".format(self.name, self.weapon)

    def talk(self):
        print("{}: I've got my {}".format(self.name, self.weapon))

    def move(self):
        print("{}: {}".format(self.name, move_quotes[random.randrange(0, len(move_quotes))]))

    def taunt(self):
        print("{}: {}".format(self.name, taunt_quote))

    def joke(self):
        print("{}: {}".format(self.name, joke_quote))

    def attack(self):
        print("{}: {}".format(self.name, attack_quotes[random.randrange(0, len(attack_quotes))]))


if __name__ == "__main__":
    try:
        olaf = Warrior("Olaf", "Axe")
        olaf.talk()
        print(olaf)
        olaf.joke()
        olaf.taunt()
        olaf.move()
        olaf.move()
        olaf.attack()
        olaf.attack()
        del olaf
    except Exception as e:
        print("Your program encountered an error.")
        print("Error:", e)
        exit(84)
    print("Congratulation !")