#!/usr/bin/python3

def number_keys(a_dictionary):
    result = 0

    for _ in a_dictionary.items():
        result += 1

    return result
