"""
Coin change problem solver using dynamic programming.

This module finds the minimum number of coins needed to make a target amount.
"""

#: Sentinel value representing impossible coin combinations
NOT_POSSIBLE = None

def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """
    Find the fewest coins needed to make the target amount.

    Uses dynamic programming to build up solutions for all amounts from 0 to target,
    keeping track of the minimum number of coins needed for each amount.

    Args:
        coins: List of available coin denominations (positive integers)
        target: Target amount to make change for (non-negative integer)

    Returns:
        Sorted list of coins that sum to target using minimum number of coins

    Raises:
        ValueError: If target is negative or cannot be made with given coins

    Example:
        >>> find_fewest_coins([1, 5, 10, 25], 30)
        [5, 25]
        >>> find_fewest_coins([2, 5], 3)
        ValueError: can't make target with given coins
    """
    if target < 0:
        raise ValueError("target can't be negative")

    change_mapping = {0: []}

    for change_value in range(1, target + 1):
        best_predecessor = NOT_POSSIBLE
        coin_to_add = None

        for coin_value in coins:
            if coin_value > change_value:
                continue

            predecessor = change_mapping[change_value - coin_value]
            if predecessor is NOT_POSSIBLE:
                continue

            if best_predecessor == NOT_POSSIBLE or len(predecessor) < len(best_predecessor):
                best_predecessor = predecessor
                coin_to_add = coin_value

        if best_predecessor == NOT_POSSIBLE:
            change_mapping[change_value] = NOT_POSSIBLE
        else:
            change_mapping[change_value] = best_predecessor + [coin_to_add]

    if change_mapping[target] == NOT_POSSIBLE:
        raise ValueError("can't make target with given coins")

    return sorted(change_mapping[target])
