#!/usr/bin/env python
from functions import *

def test_isValid():

    assert isValid('a', {'c','a','t'}, "cat") == True # True case
    assert isValid('a', {'c','b','t'}, "cat") == False # Invalid letter false case
    assert isValid('b', {'c','a','t'}, "cat") == False # Missing center letter false case

def test_isBonus():

    assert isBonus('a', {'c','a','t'}, "cat") == True # True case
    assert isBonus('a', {'c','a','t','s'}, "cat") == False # False case
