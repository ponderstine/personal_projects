#!/usr/bin/env python
from functions import *

def test_isValid():

    assert isValid('a', {'c'}, "ac", 3) == False # Too short false case
    assert isValid('a', {'c','b','t'}, "crate", 0) == False # Invalid letter false case
    assert isValid('b', {'c','a','t'}, "cat", 0) == False # Missing center letter false case
    assert isValid('a', {'c','b','t'}, "cab", 3) == True # True case

def test_isBonus():

    assert isBonus('a', {'c','a','t'}, "cat") == True # True case
    assert isBonus('a', {'c','a','t','s'}, "cat") == False # False case
