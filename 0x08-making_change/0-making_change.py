#!/usr/bin/python3
"""Module for making change using minimum number of coins
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total
    
    Args:
        coins:  List of coin values available
        total: Target amount to make change for
        
    Returns:
        int: Minimum number of coins needed, -1 if total cannot be met
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
