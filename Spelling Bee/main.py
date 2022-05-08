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
        bonus = True
        print(f"\nRound {round}: Your letters are: {mainLetter}\n{otherLetters}")
        myWord = input("Enter a word using your letters: ")

        if len(myWord) < 4:
            print("Words must be at least 4 letters long. Try again.")
            continue
        # check if quitting the game
        elif myWord == "Quit":
            print(f"\nThanks for playing! Your final score is {score}.")
            break
        
        # lowercase all letters to compare to set of lower case english words. Must be done after checking for 'Quit' since capital 'Q' is used to distinguish from the word 'quit' in the game
        myWord = myWord.lower()

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
            elif myWord in words:
                # valid word, increase score by length of word
                score += len(myWord)
        
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
                print(f"{myExc}, your score is now {score}")
            else:
                # valid letters but invalid word
                print(f"{myWord} is not a valid word. Try again!")
                continue
            
if __name__ == "__main__":
    main()