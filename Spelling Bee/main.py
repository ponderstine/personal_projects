#!/usr/bin/env python
from string import ascii_uppercase
from random import choice
from functions import *

def main():

    minLen = 3
    score = 0
    round = 0
    exclamations = ["Awesome", "Great", "Superb", "Fantastic", "Good job", "Doing great", "Keep it up"]
    vowels = ["A", "E", "I", "O", "U"]

    # randomly select letters for game
    mainLetter = choice(ascii_uppercase)
    otherLetters = {choice(vowels), choice(vowels), choice(ascii_uppercase), choice(ascii_uppercase), choice(ascii_uppercase), choice(ascii_uppercase)}

    # check that there are 6 unique other lettes
    while len(otherLetters) < 6:
        otherLetters.add(choice(ascii_uppercase))

    # check main letter is not in other letters
    while True:
        if mainLetter in otherLetters:
            mainLetter = choice(ascii_uppercase)
        else:
            break

    allLetters = otherLetters.copy()
    allLetters.add(mainLetter)
    possibleWords = []
    numWords = 0

    # read in Scrabble dictionary of words
    with open('dictionary.txt') as f:
        words = f.readlines()

    for w in words:
        # remove trailing '\n' from words
        w = w.rstrip('\n')

        # Check if word is valid with current letters
        if isValid(mainLetter, otherLetters, w, minLen):
            possibleWords.append(w)
            numWords += 1

    foundWords = []
    
    print("\nIf you want to quit, enter 'q' or 'Q'")
    print(f"Your main letter is {mainLetter}, your other letters are {otherLetters}, there are {numWords} words that can be made with these letters.")
    
    # game loop
    while True:
        round += 1
        isBreak = False
        bonus = True
        print(f"\nRound {round}: Your letters are: {mainLetter}\n{otherLetters}")
        myWord = input("Enter a word using your letters: ")

        # uppercase all letters to compare to set of uppercase english words
        myWord = myWord.upper()

        # check if quitting the game
        if myWord == "Q":
            print(f"\nThanks for playing! You found {len(foundWords)}/{len(possibleWords)} words. Your final score is {score}.")
            break
        elif len(myWord) < minLen:
            print(f"Words must be at least {minLen} letters long. Try again.")
            continue

        # check if word contains main letter
        if mainLetter not in myWord:
            print(f"{myWord} does not include the main letter.")
            continue
        else:
            # check that all letters in word are valid
            for c in myWord:
                if c not in allLetters:
                    print(f"{myWord} contains unavailable letters")
                    isBreak = True
                    break

            if isBreak:
                # word contained invalid letter so don't need to check against all words
                continue
            # check that current word has not already been found
            elif myWord in foundWords:
                print(f"You have already found the word {myWord}! Nice try ;)")
                continue
            # valid word, increase score by length of word
            elif myWord in possibleWords:
                score += len(myWord)
                foundWords.append(myWord)
        
                # loop through all 7 available letters and if one is not present then no bonus, if get to end of 7 letters without missing a letter in the word then bonus stays True
                for c in allLetters:
                    if c not in myWord:
                        bonus = False
                        break
                
                # check for bonus if word contains all 7 letters at least once
                if(bonus):
                    score += 5
                    print(f"{myWord} uses all the letters! Here's a bonus")
                
                myExc = choice(exclamations)
                print(f"{myExc}, you've found {len(foundWords)}/{len(possibleWords)} words, your score is now {score}")
            else:
                # valid letters but invalid word
                print(f"{myWord} is not a valid word. Try again!")
                continue
            
if __name__ == "__main__":
    main()