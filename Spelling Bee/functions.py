#!/usr/bin/env python

def isValid(mainLetter, otherLetters, word):
    hasMain = False
    for c in word:
        if ~hasMain and c == mainLetter:
            hasMain = True
        if c not in otherLetters:
            return False
    return hasMain

def isBonus(mainLetter, otherLetters, word):
    if mainLetter not in word:
        return False
    for c in otherLetters:
        if c not in word:
            return False
    return True