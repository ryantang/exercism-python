class Infinity:
    """Implements an infinite iterable for NOT_POSSIBLE"""

    def __len__(self):
        """Max length of an 32 bit list in python"""
        return 2 ^ 31 - 1

    def __add__(self, _ignored):
        """If you add anything to infinity, it's still infinity"""
        return Infinity()

    def __eq__(self, other):
        """For our purposes, all infinities are equal"""
        return isinstance(other, Infinity)

NOT_POSSIBLE = Infinity()

def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    if target < 0:
        raise ValueError("target can't be negative")

    change_mapping = {0: []}

    for change_value in range(1, target + 1):

        best_predecessor = NOT_POSSIBLE
        coin_to_add = None

        for coin_value in coins:
            if (coin_value <= change_value
                and len(change_mapping[change_value - coin_value]) < len(best_predecessor)):
                best_predecessor = change_mapping[change_value - coin_value]
                coin_to_add = coin_value

        change_mapping[change_value] = best_predecessor + [coin_to_add]

    if change_mapping[target] == NOT_POSSIBLE:
        raise ValueError("can't make target with given coins")

    return sorted(change_mapping[target])
