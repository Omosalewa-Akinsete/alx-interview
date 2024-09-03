#!/usr/bin/python3
"""Maria and Ben playing a game"""

def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of a game where Maria and Ben
    take turns picking prime numbers and removing them and their multiples
    from a set of consecutive integers.

    Args:
        x (int): The number of rounds to be played.
        nums (list of int): A list where each element is 'n', representing
                            the range of numbers from 1 to n for each round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben").
             Returns None if the winner cannot be determined.
    """

    def sieve_of_eratosthenes(max_num):
        """
        Implements the Sieve of Eratosthenes algorithm to find all prime numbers
        up to a given number.

        Args:
            max_num (int): The maximum number to check for primes.

        Returns:
            list of int: A list of all prime numbers up to 'max_num'.
        """
        sieve = [True] * (max_num + 1)  # Initialize sieve array
        sieve[0] = sieve[1] = False  # 0 and 1 are not primes
        p = 2
        # Mark non-primes as False
        while p * p <= max_num:
            if sieve[p]:
                for i in range(p * p, max_num + 1, p):
                    sieve[i] = False
            p += 1
        # Return list of primes
        return [p for p in range(max_num + 1) if sieve[p]]

    def play_game(n):
        """
        Simulates a single round of the game.

        Args:
            n (int): The range of numbers from 1 to n.

        Returns:
            str: The winner of the game ("Maria" or "Ben").
        """
        primes = sieve_of_eratosthenes(n)  # Get all primes up to n
        is_maria_turn = True  # Maria starts the game
        prime_set = set(primes)  # Set of primes for fast removal

        # Players take turns removing primes and their multiples
        while prime_set:
            prime = next(iter(prime_set))  # Maria picks the smallest prime
            multiples = set(range(prime, n + 1, prime))  # Remove prime and its multiples
            prime_set -= multiples  # Update the set of remaining primes
            is_maria_turn = not is_maria_turn  # Switch turns

        # If it's Maria's turn and there are no primes left, Ben wins
        return "Ben" if is_maria_turn else "Maria"

    # Initialize win counters for both players
    maria_wins = 0
    ben_wins = 0

    # Simulate each round of the game
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner after all rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
