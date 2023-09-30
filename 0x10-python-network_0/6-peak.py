#!/bin/python3
"""Write a function that finds a peak in a list of unsorted integers.
    Prototype: def find_peak(list_of_integers):
    You are not allowed to import any module
    Your algorithm must have the lowest complexity
    (hint: you don’t need to go through all numbers to find a peak)
    6-peak.py must contain the function
    6-peak.txt must contain the complexity of your algorithm:
    `O(log(n))`, `O(n)`,`O(nlog(n))` or `O(n2)`
    Note: there may be more than one peak in the list
"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not isinstance(list_of_integers, list):
        return
    peak = []
    for idx in range(len(list_of_integers)):
        if idx == 0:
            if list_of_integers[idx] >= list_of_integers[idx + 1]:
                peak.append(list_of_integers[idx])
        elif idx == len(list_of_integers) - 1:
            if list_of_integers[idx] >= list_of_integers[idx - 1]:
                peak.append(list_of_integers[idx])
        else:
            if list_of_integers[idx] >= list_of_integers[idx - 1] and\
                    list_of_integers[idx] >= list_of_integers[idx + 1]:
                peak.append(list_of_integers[idx])
    return max(peak) if peak else None
