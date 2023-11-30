#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if not list_of_integers:
        return None

    lo = 0
    hi = len(list_of_integers) - 1  # Adjusted to avoid out-of-bounds access
    mid = (hi + lo) // 2

    if hi == lo:
        return list_of_integers[lo]
    if hi == lo + 1:
        return max(list_of_integers[lo], list_of_integers[hi])

    if list_of_integers[mid] >= list_of_integers[mid - 1] and \
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])
    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
