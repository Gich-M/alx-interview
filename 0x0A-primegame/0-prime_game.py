#!/usr/bin/python3

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    """Get all primes up to and including n."""
    return [x for x in range(2, n + 1) if is_prime(x)]

def play_game(n):
    """Simulate a single round of the Prime Game.
    Returns True if Maria wins, False if Ben wins."""
    primes = get_primes(n)

    maria_turn = True
    turn_count = 0

    while primes:
        turn_count += 1

        curr_prime = primes[0]

        primes = [p for p in primes if p % curr_prime != 0]

        maria_turn = not maria_turn

    result = not maria_turn
    return result

def isWinner(x, nums):
    """Determine the overall winner of x rounds."""
    if not nums or x == 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
