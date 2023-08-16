#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0

    if type(roman_string) is not str:
        return 0

    list_of_values = {"I": 1, "V": 5, "X": 10,
                      "L": 50, "C": 100, "D": 500,
                      "M": 1000}

    result = []
    w_val = 0
    new_val = []

    for value in roman_string:
        for k, v in list_of_values.items():
            if k == value:
                result.append(v)

    if len(result) == 1:
        return result[0]
    elif result[0] < result[1]:
        w_val = (result[0] - result[1]) * (-1)
        if len(result[2:]) != 0:
            new_val = list(map(lambda x: x + w_val, result[2:]))
            return sum(new_val)
    else:
        return sum(result)
