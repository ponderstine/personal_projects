#!/usr/bin/env python
from english_words import english_words_lower_set as words
from string import ascii_lowercase
from random import choice

def main():

    # randomly select letters for game
    mainLetter = choice(ascii_lowercase)
    otherLetters = {choice(ascii_lowercase), choice(ascii_lowercase), choice(ascii_lowercase), choice(ascii_lowercase), choice(ascii_lowercase), choice(ascii_lowercase)}
    print(otherLetters)

    print(len(otherLetters))

    # check that there are 6 unique other lettes
    while len(otherLetters) < 6:
        otherLetters.add(choice(ascii_lowercase))

    print(otherLetters)

    print(len(otherLetters))

    print(mainLetter)

    # check main letter is not in other letters
    while True:
        if mainLetter in otherLetters:
            mainLetter = choice(ascii_lowercase)
        else:
            break
    
    print(mainLetter)

    # myWord = input("Type a valid word: ")
    # print("You input: " + myWord)
    # if myWord in words:
    #     print("You entered a valid word")
    # else:
    #     print("You did NOT enter a valid word")

if __name__ == "__main__":
    main()