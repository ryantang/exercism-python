from collections import Counter

RANKS = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10": 10,
    "J" : 11,
    "Q" : 12,
    "K" : 13,
    "A" : 14,
}

WHEEL_CHECK = [2, 3, 4, 5, 14]
WHEEL_RANK = [1, 2, 3, 4, 5]


def best_hands(hands):
    if _straight_flush(hands):
        return _best_straight_flush(hands)
    if _four_of_a_kind(hands):
        return _best_four_of_a_kind(hands)
    if _full_house(hands):
        return _best_full_house(hands)
    if _flush(hands):
        return _best_flush(hands)
    if _straight(hands):
        return _best_straight(hands)
    if _three_of_a_kind(hands):
        return _best_three_of_a_kind(hands)
    if _two_pair(hands):
        return _best_two_pair(hands)
    if _pair(hands):
        return _best_pair(hands)
    return _best_high_card(hands)

def _best_straight_flush(hands):
    straight_flush_hands = [hand for hand in hands if _has_straight_flush(hand)]
    return _best_high_card(straight_flush_hands)

def _straight_flush(hands):
    return any(_has_straight_flush(hand) for hand in hands)

def _has_straight_flush(hand):
    return _has_straight(hand) and _has_flush(hand)

def _best_by_rank_groups(hands, filter_fn, rank_fn):
    """Generic helper to find best hands by comparing rank groups such as
    four-of-a-kinds, three-of-a-kind, two pairs.
    
    Args:
        hands: All hands to compare
        filter_fn: Function to filter qualifying hands (e.g., _has_pair)
        rank_fn: Function to extract comparable ranks (e.g., _pair_ranks)
    """
    qualified_hands = [hand for hand in hands if filter_fn(hand)]
    if len(qualified_hands) < 2:
        return qualified_hands

    # A "set" here means matching cards (pairs, trips, quads).
    # For two-pair, sets is a list of both pair values: [10, 3] means pair of 10s and pair of 3s
    # Cache set calculations to avoid repeated function calls
    hands_with_sets = [
        (hand, sorted(rank_fn(hand), reverse=True))
        for hand in qualified_hands
    ]

    best_sets = max(sets for _hand, sets in hands_with_sets)
    hands_with_best_sets = [hand for hand, sets in hands_with_sets if sets == best_sets]

    return _best_high_card(hands_with_best_sets)

def _best_four_of_a_kind(hands):
    return _best_by_rank_groups(hands, _has_four_of_a_kind, _quad_ranks)

def _quad_ranks(hand):
    return [rank for rank, count in _counts(hand).items() if count == 4]

def _four_of_a_kind(hands):
    return any(_has_four_of_a_kind(hand) for hand in hands)

def _has_four_of_a_kind(hand):
    return any(count == 4 for count in _counts(hand).values())

def _best_full_house(hands):
    full_house_hands = [hand for hand in hands if _has_full_house(hand)]

    return _best_three_of_a_kind(full_house_hands)

def _full_house(hands):
    return any(_has_full_house(hand) for hand in hands)

def _has_full_house(hand):
    return _has_three_of_a_kind(hand) and _has_pair(hand)


def _best_flush(hands):
    flush_hands = [hand for hand in hands if _has_flush(hand)]

    return _best_high_card(flush_hands)


def _flush(hands):
    return any(_has_flush(hand) for hand in hands)

def _has_flush(hand):
    return any(count == 5 for count in _suit_counts(hand).values())

def _best_straight(hands):
    straight_hands = [hand for hand in hands if _has_straight(hand)]
    return _best_high_card(straight_hands)


def _straight(hands):
    return any(_has_straight(hand) for hand in hands)


def _has_straight(hand):
    card_values = _ranks(hand)
    low_card = min(card_values)
    five_in_a_row = list(range(low_card, low_card + 5))

    return sorted(card_values) == five_in_a_row


def _best_three_of_a_kind(hands):
    return _best_by_rank_groups(hands, _has_three_of_a_kind, _trips_ranks)

def _trips_ranks(hand):
    return [rank for rank, count in _counts(hand).items() if count == 3]


def _three_of_a_kind(hands):
    return any(_has_three_of_a_kind(hand) for hand in hands)

def _has_three_of_a_kind(hands):
    return any(count == 3 for count in _counts(hands).values())

def _two_pair(hands):
    return any(_has_two_pair(hand) for hand in hands)

def _best_two_pair(hands):
    return _best_by_rank_groups(hands, _has_two_pair, _pair_ranks)


def _has_two_pair(hand):
    return len(_pair_ranks(hand)) == 2

def _best_pair(hands):
    return _best_by_rank_groups(hands, _has_pair, _pair_ranks)


def _pair_ranks(hand):
    return [rank for rank, count in _counts(hand).items() if count == 2]

def _pair(hands):
    return any(_has_pair(hand) for hand in hands)

def _has_pair(hand):
    return any(count == 2 for count in _counts(hand).values())

def _counts(hand):
    return Counter(_ranks(hand))

def _suit_counts(hand):
    return Counter(card[-1] for card in hand.split())


def _best_high_card(hands):
    hands_with_sorted_ranks = [
        (hand, sorted(_ranks(hand), reverse=True))
        for hand in hands
    ]

    highest_ranks = max(ranks for _hand, ranks in hands_with_sorted_ranks)
    return [hand for hand, ranks in hands_with_sorted_ranks if ranks == highest_ranks]

def _ranks(hand):
    ranks = [RANKS[card[:-1]] for card in hand.split()]
    if sorted(ranks) == WHEEL_CHECK:
        return WHEEL_RANK

    return ranks
