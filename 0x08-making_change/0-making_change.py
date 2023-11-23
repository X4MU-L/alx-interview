#!/usr/bin/python3

"""
Create a function makeChange and check the fewest coins
needed to make total
"""


def recurseChange(sorted_coins: list, total: int, cum: int) -> int:
    """
    recursively make coins changes from the available coins for the total
    Args:
        sorted_coins: list of non-negative numbers
        total: int
        cum: int
    """
    coinlength = len(sorted_coins) - 1
    if total != 0 and coinlength < 0:
        return -1

    if total == 0:
        return cum

    elif total % sorted_coins[coinlength] == 0:
        cum += total // sorted_coins[coinlength]
        total = total % sorted_coins[coinlength]
        return cum

    while total - sorted_coins[coinlength] > 0:
        total = total - sorted_coins[coinlength]
        cum += 1
    return recurseChange(sorted_coins[: coinlength], total, cum)


def makeChange(coins: list, total: int) -> int:
    """
    make change for the fewest coin possible for total
    Args
        coins: list of non-negative numbers
        total: int
    """
    if total <= 0:
        return 0

    if not isinstance(coins, list):
        return -1
    coins.sort()
    return recurseChange(coins, total, 0)
