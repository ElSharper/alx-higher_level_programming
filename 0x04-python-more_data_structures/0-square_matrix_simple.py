#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = list()
    for rw in matrix:
        new_list.append(list(map(
            lambda x: x**2, rw)))
    return new_list
