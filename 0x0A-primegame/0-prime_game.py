#!/usr/bin/python3
"""Maria and Ben playing a game"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(max_num):
        sieve = [True] * (max_num + 1)
        sieve[0] = sieve[1] = False
        p = 2
        while p * p <= max_num:
            if sieve[p]:
                for i in range(p * p, max_num + 1, p):
                    sieve[i] = False
            p += 1
        return [p for p in range(max_num + 1) if sieve[p]]

    def play_game(n):
        primes = sieve_of_eratosthenes(n)
        is_maria_turn = True
        prime_set = set(primes)

        while prime_set:
            prime = next(iter(prime_set))
            multiples = set(range(prime, n + 1, prime))
            prime_set -= multiples
            is_maria_turn = not is_maria_turn

        return "Ben" if is_maria_turn else "Maria"

    # Two blank lines after this function, as required by PEP 8

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
i
