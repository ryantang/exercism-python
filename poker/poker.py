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

def _best_flush(hands):
    flush_hands = [hand for hand in hands if _has_flush(hand)]

    return flush_hands


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
    three_of_a_kind_hands = [hand for hand in hands if _has_three_of_a_kind(hand)]
    if len(three_of_a_kind_hands) < 2:
        return three_of_a_kind_hands

    best_three_of_a_kind_hands = [three_of_a_kind_hands[0]]
    for hand in three_of_a_kind_hands[1:]:
        sorted_best_triples = sorted(_trips_ranks(best_three_of_a_kind_hands[0]), reverse=True)
        sorted_hand_triples = sorted(_trips_ranks(hand), reverse=True)
        if sorted_hand_triples > sorted_best_triples:
            best_three_of_a_kind_hands = [hand]
        elif sorted_hand_triples == sorted_best_triples:
            best_three_of_a_kind_hands.append(hand)

    return _best_high_card(best_three_of_a_kind_hands)

def _trips_ranks(hand):
    return [rank for rank, count in _counts(hand).items() if count == 3]


def _three_of_a_kind(hands):
    return any(_has_three_of_a_kind(hand) for hand in hands)

def _has_three_of_a_kind(hands):
    return any(count == 3 for count in _counts(hands).values())

def _two_pair(hands):
    return any(_has_two_pair(hand) for hand in hands)

def _best_two_pair(hands):
    two_paired_hands = [hand for hand in hands if _has_two_pair(hand)]
    if len(two_paired_hands) < 2:
        return two_paired_hands

    best_two_paired_hands = [two_paired_hands[0]]
    for hand in hands[1:]:
        sorted_best_pairs = sorted(_pair_ranks(best_two_paired_hands[0]), reverse=True)
        sorted_hand_pairs = sorted(_pair_ranks(hand), reverse=True)
        if sorted_hand_pairs > sorted_best_pairs:
            best_two_paired_hands = [hand]
        elif sorted_hand_pairs == best_two_paired_hands:
            best_two_paired_hands.append(hand)
    return _best_high_card(best_two_paired_hands)


def _has_two_pair(hand):
    return len(_pair_ranks(hand)) == 2

def _best_pair(hands):
    paired_hands = [hand for hand in hands if _has_pair(hand)]
    if len(paired_hands) < 2:
        return paired_hands

    best_paired_hands = [paired_hands[0]]
    for hand in paired_hands[1:]:
        if _pair_ranks(hand) > _pair_ranks(best_paired_hands[0]):
            best_paired_hands = [hand]
        elif _pair_ranks(hand)[0] == _pair_ranks(best_paired_hands[0])[0]:
            best_paired_hands.append(hand)
    return _best_high_card(best_paired_hands)


def _pair_ranks(hand):
    return [
        rank
        for rank, count in _counts(hand).items()
        if count == 2
    ]

def _pair(hands):
    return any(_has_pair(hand) for hand in hands)

def _has_pair(hand):
    return any(count == 2 for count in _counts(hand).values())

def _counts(hand):
    return Counter(_ranks(hand))

def _suit_counts(hand):
    suits = [card[-1] for card in hand]
    return Counter(suits)


def _best_high_card(hands):
    best_high_card_hands = [hands[0]]
    for hand in hands[1:]:
        sorted_best = sorted(_ranks(best_high_card_hands[0]), reverse=True)
        sorted_hand = sorted(_ranks(hand), reverse=True)
        if sorted_hand > sorted_best:
            best_high_card_hands = [hand]
        elif sorted_hand == sorted_best:
            best_high_card_hands.append(hand)

    return best_high_card_hands

def _ranks(hand):
    ranks = [RANKS[card[:-1]] for card in hand.split()]
    if sorted(ranks) == WHEEL_CHECK:
        return WHEEL_RANK

    return ranks
