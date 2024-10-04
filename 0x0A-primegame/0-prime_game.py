#!/usr/bin/python3
"""Module function function."""


def isWinner(x, nums):
    """Function who wh"""
    mariamore = 0
    bnmore = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            bnmore += 1
            continue

        isMariaTurns = True

        while(True):
            if not primesSet:
                if isMariaTurns:
                    bnmore += 1
                else:
                    mariamore += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

    if mariamore > bnmore:
        return "Winner: Maria"

    if mariamore < bnmore:
        return "Winner: Ben"

    return None


def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes
