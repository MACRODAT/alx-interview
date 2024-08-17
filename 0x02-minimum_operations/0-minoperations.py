#!/usr/bin/python3
"""
Function for calculating number of operations
"""


def minOperations(n):
    a = 1
    if n == 1:
        return 0
    while True:
        a += 1
        if n % a == 0:
            return a + minOperations(n // a)
        if a == n-1:
            break
    return n
