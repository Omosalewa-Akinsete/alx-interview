#!/usr/bin/python3
"""Maria and Ben playing a game"""


def is_prime(n):
    """
    Checks if number is a prime

    Args:
        n (int): Number

    Return:
        True if n is a prime, else False
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_numbers(start, end):
    """
    Returns a list of prime numbers from start to end (inclusive)

    Args:
        start (int): Start number
        end (int): Last number to include
    """
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes


def isWinner(x, nums):
    """
    Determines the winner of a prime numbers game

    Args:
        x (int): The number of rounds
        nums (list): An array

    Return:
        name of player who won the most rounds
        None, if the winner cannot be determined
    """

    winner = None

    if not nums or x < 1:
        return winner

    mariaCount = 0
    benCount = 0

    for num in nums:
        rounds = list(range(1, num + 1))
        primes = prime_numbers(1, num)

        if not primes:
            benCount += 1
            continue

        maria_turn = True

        while (True):
            if not primes:
                if maria_turn:
                    benCount += 1
                else:
                    mariaCount += 1
                break

            leastPrime = primes.pop(0)
            rounds.remove(leastPrime)

            rounds = [x for x in rounds if x % leastPrime != 0]

            maria_turn = not maria_turn

    if mariaCount > benCount:
        winner = "Maria"

    if benCount > mariaCount:
        winner = "Ben"

    return winner
