"""Scores the Yacht dice game."""

from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice: list, category: str) -> int:
    """
    Calculates the score from a round of the Yacht dice game
    
    :param dice: List of five rolled dice values
    :type dice: list
    :param category: Category which these dice should be scored by (denoted by constants above)
    :type category: str
    :return: Score of the dice for the given category
    :rtype: int
    """
    if len(dice) != 5:
        raise ValueError("Must roll five dice")

    dice_counts = Counter(dice)

    if category == YACHT:
        return (50 if len(dice_counts) == 1 else 0)
    if category == ONES:
        return dice_counts[1]
    if category == TWOS:
        return dice_counts[2] * 2
    if category == THREES:
        return dice_counts[3] * 3
    if category == FOURS:
        return dice_counts[4] * 4
    if category == FIVES:
        return dice_counts[5] * 5
    if category == SIXES:
        return dice_counts[6] * 6
    if category == FULL_HOUSE:
        return (sum(dice) if set(dice_counts.values()) == {2, 3} else 0)
    if category == FOUR_OF_A_KIND:
        return next((roll * 4 for roll, count in dice_counts.items() if count >= 4), 0)
    if category == LITTLE_STRAIGHT:
        return (30 if set(dice) == {1, 2, 3, 4, 5} else 0)
    if category == BIG_STRAIGHT:
        return (30 if set(dice) == {2, 3, 4, 5, 6} else 0)
    if category == CHOICE:
        return sum(dice)

    return 0
