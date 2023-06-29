#!/usr/bin/python3
#write a function scriptfinding peak in list of ints, interview prep

def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """i
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
