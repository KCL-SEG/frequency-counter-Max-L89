"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    # Your code goes here
    for x in items:
        x=str(x)
        if x in frequencies:
            frequencies[x] += 1
        else:
            frequencies[x] = 1

    return frequencies
