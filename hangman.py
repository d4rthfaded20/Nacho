import random
from words import words_list

# Build a hangman game here
###print(words_list)

hangman_art = {0:("    ",
                  "    ",
                  "    "),
               1: (" o  ",
                  "     ",
                  "     "),
               2: (" o  ",
                   " |  ",
                   "    "),
               3: (" o  ",
                  "  |  ",
                  " /   "),
               4: ("  o  ",
                   "  |\\  ",
                   " /   "),
               5: ("  o  ",
                   "  |\\  ",
                   " / \\  "),
               6: ("  o  ",
                   " /|\\  ",
                   " / \\  ")}
word = random.choice(words_list)
tries = 6

print (word)
for line in hangman_art[0: +tries]:
    print (line)

def display_man(wrong_guesses):
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass


if input(tries) == (word):
