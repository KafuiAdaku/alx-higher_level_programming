#!/usr/bin/python3

def multiple_returns(sentence):
    multi_tuple = (0,)

    if len(sentence) == 0:
        multi_tuple = (0,sentence[0] == "None")
        return multi_tuple
    else:
        multi_tuple = (len(sentence), sentence[0])
        return multi_tuple

