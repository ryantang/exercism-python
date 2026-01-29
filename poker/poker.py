RANK = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def best_hands(hands):
    return _best_high_card_hands(hands)

def _best_high_card_hands(hands):
    best_high_card_hands = [hands[0]]
    for hand in hands[1:]:
        sorted_best = sorted(_ranks(best_high_card_hands[0]),reverse=True)
        sorted_hand = sorted(_ranks(hand), reverse=True)

        if sorted_hand > sorted_best:
            best_high_card_hands = [hand]
        elif sorted_hand == sorted_best:
            best_high_card_hands.append(hand)

    return best_high_card_hands

def _ranks(hand):
    card_values = []
    for card in hand.split():
        card_values.append(RANK[card[:-1]])

    return card_values
