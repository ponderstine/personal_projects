#!/usr/bin/env python
from english_words import english_words_lower_set as words

def main():
    myWord = input("Type a valid word: ")
    string = "You input: " + myWord
    print(string)
    if myWord in words:
        print("You entered a valid word")
    else:
        print("You did NOT enter a valid word")

if __name__ == "__main__":
    main()