#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or len(roman_string) == 0:
        return 0
    
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    for c in roman_string:
        if c in roman_numerals:
            value = roman_numerals[c]
            result += value
            if value > prev_value:
                result -= 2 * prev_value
            prev_value = value
        else:
            return 0
    
    return result
