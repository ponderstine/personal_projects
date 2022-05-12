#!/usr/bin/env python

def isValid(mainLetter, otherLetters, word, min):
    if len(word) < min:
        return False
    
    hasMain = False
    for c in word:
        if c == mainLetter:
            hasMain = True
        elif c not in otherLetters:
            return False
    return hasMain

def isBonus(mainLetter, otherLetters, word):
    if mainLetter not in word:
        return False
    for c in otherLetters:
        if c not in word:
            return False
    return True