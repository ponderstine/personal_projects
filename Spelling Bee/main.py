#!/usr/bin/env python
from english_words import english_words_lower_set as words
from string import ascii_lowercase
from random import choice

def main():

    score = 0
    round = 0
    exclamations = ["Awesome", "Great", "Superb"]

    # randomly select letters for game
    mainLetter = choice(ascii_lowercase)
    otherLetters = {choice(ascii_lowercase), choice(ascii_lowercase), choice(ascii_lowercase), choice(ascii_lowercase), choice(ascii_lowercase), choice(ascii_lowercase)}

    # check that there are 6 unique other lettes
    while len(otherLetters) < 6:
        otherLetters.add(choice(ascii_lowercase))

    # check main letter is not in other letters
    while True:
        if mainLetter in otherLetters:
            mainLetter = choice(ascii_lowercase)
        else:
            break

    allLetters = otherLetters.copy()
    allLetters.add(mainLetter)
    
    print("\nIf you want to quit, type 'Quit (capital Q)'")
    
    # game loop
    while True:
        round += 1
        isBreak = False
        print(f"\nRound {round}: Your letters are: {mainLetter}\n{otherLetters}")
        myWord = input("Enter a word using your letters: ")

        # check if quitting the game
        if myWord == "Quit":
            print(f"\nThanks for playing! Your final score is {score}.")
            break
        elif mainLetter not in myWord:
            print(f"{myWord} does not include the main letter.")
            break
        else:
            for c in myWord:
                if c not in allLetters:
                    print(f"{myWord} contains unavailable letters")
                    isBreak = True
                    break
            if isBreak:
                continue
            elif myWord in words:
                # valid word, increase score by length of word
                score += len(myWord)
                myExc = choice(exclamations)
                print(f"{myExc}, your score is now {score}")
            else:
                # valid letters but invalid word
                print(f"{myWord} is not a valid word. Try again!")
                continue
            
if __name__ == "__main__":
    main()