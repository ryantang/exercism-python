from collections import defaultdict

VALUES = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14,
}

HAND_SIZE = 5


def best_hands(hands) -> list[str]:
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
    if _any_pair(hands):
        return _best_pair(hands)
    return _high_card(hands)

def _best_four_of_a_kind(hands):
    four_of_a_kind_hands = [
        hand for hand in hands
        if _has_four_of_a_kind(hand)
    ]

    if len(four_of_a_kind_hands) > 1:
        best_four_of_a_kind_hands = [four_of_a_kind_hands[0]]
        for hand in hands[1:]:
            if _quads(hand)[0] > _quads(best_four_of_a_kind_hands[0])[0]:
                best_four_of_a_kind_hands = [hand]
            elif _quads(hand)[0] == _quads(best_four_of_a_kind_hands[0])[0]:
                best_four_of_a_kind_hands.append(hand)

        return _high_card(best_four_of_a_kind_hands)

    return four_of_a_kind_hands

def _quads(hand):
    return [
        card_value
        for card_value, count in _counts(hand).items()
        if count == 4
    ]

def _four_of_a_kind(hands):
    return any(_has_four_of_a_kind(hand) for hand in hands)

def _has_four_of_a_kind(hand):
    return bool(_quads(hand))

def _full_house(hands):
    return any(_has_full_house(hand) for hand in hands)

def _has_full_house(hand):
    return _trips(hand) and _has_pair(hand)

def _best_full_house(hands):
    full_house_hands = [
        hand for hand in hands
        if _has_full_house(hand)
    ]

    return _best_three_of_a_kind(full_house_hands)


def _flush(hands):
    return any(_has_flush(hand) for hand in hands)

def _has_flush(hand):
    return any(count==5 for count in _suit_counts(hand).values())


def _best_flush(hands):
    flush_hands = [hand for hand in hands if _has_flush(hand)]

    return _high_card(flush_hands)

def _straight(hands):
    return any(_is_straight(hand) for hand in hands)

def _is_straight(hand)->bool:
    card_values = _values_with_low_ace(hand)
    low_card = min(card_values)
    five_in_a_row = range(low_card, low_card + HAND_SIZE)
    return set(card_values) == set(five_in_a_row)


def _best_straight(hands):
    straight_hands = [
        hand for hand in hands
        if _is_straight(hand)
    ]

    return _high_card(straight_hands)

def _values_with_low_ace(hand):
    card_values = _values(hand)

    # Ace is counted as 1 if it's part of a low straight
    if 14 in card_values:
        low_ace_card_values = card_values.copy()
        low_ace_card_values.remove(14)
        low_ace_card_values.append(1)
        low_card = min(low_ace_card_values)
        five_in_a_row = range(low_card, low_card + HAND_SIZE)

        # check if straight
        if set(low_ace_card_values) == set(five_in_a_row):
            return low_ace_card_values

    return card_values


def _best_three_of_a_kind(hands):
    trip_hands = [
        hand
        for hand in hands
        if _trips(hand)
    ]

    if len(trip_hands) > 1:
        best_trip_hands = [trip_hands[0]]
        for hand in trip_hands[1:]:
            if _trips(hand)[0] > _trips(best_trip_hands[0])[0]:
                best_trip_hands = [hand]
            elif _trips(hand)[0] == _trips(best_trip_hands[0])[0]:
                best_trip_hands.append(hand)

        return _high_card(best_trip_hands)

    return trip_hands



def _trips(hand):
    return [
        face_value
        for face_value, count in _counts(hand).items()
        if count == 3
    ]

def _three_of_a_kind(hands):
    return any(_trips(hand) for hand in hands)


def _best_two_pair(hands):
    two_paired_hands = [
        hand
        for hand in hands
        if len(_pairs(hand)) == 2
    ]

    if len(two_paired_hands) > 1:
        highest_two_paired_hands = [two_paired_hands[0]]
        for hand in two_paired_hands[1:]:
            highest_pairs = sorted(_pairs(highest_two_paired_hands[0]))[::-1]
            hand_pairs = sorted(_pairs(hand))[::-1]

            if hand_pairs[0] > highest_pairs[0]:
                highest_two_paired_hands = [hand]
            elif highest_pairs[0] == hand_pairs[0] and hand_pairs[1] > highest_pairs[1]:
                highest_two_paired_hands = [hand]
            elif highest_pairs[0] == hand_pairs[0] and highest_pairs[1] == hand_pairs[1]:
                highest_two_paired_hands.append(hand)

        return _high_card(highest_two_paired_hands)

    return two_paired_hands

def _two_pair(hands):
    for hand in hands:
        if len(_pairs(hand)) == 2:
            return True

    return False


def _best_pair(hands):
    paired_hands = [hand for hand in hands if _has_pair(hand)]

    if len(paired_hands) > 1:
        if len(_highest_pair(paired_hands)) == 1:
            return _highest_pair(paired_hands)
        return _high_card(paired_hands)

    return paired_hands

def _highest_pair(paired_hands):
    highest_paired_hands = [paired_hands[0]]
    highest_pair = _pairs(highest_paired_hands[0])[0] #assume we only have one pair

    for hand in paired_hands[1:]:
        if _pairs(hand)[0] > highest_pair:
            highest_paired_hands = [hand]
            highest_pair = _pairs(hand)[0]
        elif _pairs(hand)[0] > highest_pair:
            highest_paired_hands.append(hand)

    return highest_paired_hands

def _any_pair(hands):
    return any(_has_pair(hand) for hand in hands)

def _has_pair(hand):
    return any(_pairs(hand))

def _pairs(hand):
    return [
        card_value
        for card_value, count in _counts(hand).items()
        if count == 2
    ]

def _counts(hand: str)-> dict[int, int]:
    """
    Given a poker hand, _counts returns a dictionary with card face values as keys
    and the number of those cards as the value.

    Example: "2H 7S KC 3H 7D" becomes 
        {
        2: 1, 
        7: 2, #hand has two 7's
        13: 1, #king is converted to 13
        3: 1
        }
    """
    counts = defaultdict(int)
    for card in _values(hand):
        counts[card] += 1

    return counts


def _high_card(hands):
    high_card_hands = [hands[0]]

    for hand in hands[1:]:
        if _higher_card_hand(high_card_hands[0], hand) == "right":
            high_card_hands = [hand]
        elif _higher_card_hand(high_card_hands[0], hand) == "both":
            high_card_hands.append(hand)

    return high_card_hands

def _higher_card_hand(left, right):
    sorted_left = sorted(_values_with_low_ace(left))[::-1]
    sorted_right = sorted(_values_with_low_ace(right))[::-1]

    for i in range(HAND_SIZE):
        if sorted_left[i] > sorted_right[i]:
            return "left"
        if sorted_right[i] > sorted_left[i]:
            return "right"
    return "both"

def _values(hand) -> list[str]:
    """
    Returns just the values of the hand without the suit
    
    :param hand: Description
    """
    return [
        VALUES[card[:-1]]
        for card in hand.split()
    ]

def _suit_counts(hand) -> dict[str, int]:
    """
    Given a poker hand, _suit_counts returns a dictionary with suit as keys
    and the number of cards of that suit as the value.    

    Example: "2H 7S KC 3H 7D" becomes {H: 2, S: 1, C: 1, D: 1}
    """
    suit_counts = defaultdict(int)
    for card in hand.split():
        suit_counts[card[-1]] += 1

    return suit_counts
