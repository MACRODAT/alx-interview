#!/usr/bin/python3
"""
Function for calculating number of operations
"""


def minOperations2(n):
    a = 1
    q = 0
    if n == 1:
        return 1
    while True:
        a += 1
        if n % a == 0:
            return a + minOperations2(n // a)
        if a == n-1:
            break
    return n
