#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dic_List = sorted(list(a_dictionary))
    for var in dic_List:
        print("{}: {}".format(var, a_dictionary[var]))
