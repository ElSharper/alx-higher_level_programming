#!/usr/bin/python3

def best_score(a_dictionary):
    vlu = 0
    kiy = ""
    if a_dictionary is None:
        return None
    for key, val in a_dictionary.items():
        if val > vlu:
            kiy = key
            vlu = val
    return kiy
