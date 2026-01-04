WORDS = {
    10: "Ten",
    9: "Nine",
    8: "Eight",
    7: "Seven",
    6: "Six",
    5: "Five",
    4: "Four",
    3: "Three",
    2: "Two",
    1: "One",
    0: "No",
}

def recite(start, take=1) -> list[str]:
    """Generate lyrics for the bottle song, starting from 'start' and taking 'take' verses."""
    verses = [_single_verse(start-i) for i in range(take)]
    return _interleave_newlines(verses)


def _single_verse(number) -> list[str]:
    """Generate the four lines of a single verse for the given bottle count."""
    count = WORDS[number]
    bottles = _pluralize_bottle(number)
    count_next = WORDS[number-1].lower()
    bottles_next = _pluralize_bottle(number-1)

    return [
        f"{count} green {bottles} hanging on the wall,",
        f"{count} green {bottles} hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        f"There'll be {count_next} green {bottles_next} hanging on the wall.",
    ]


def _interleave_newlines(verses) -> list[str]:
    """Flatten verses into a single list with empty strings between each verse."""
    result = []
    for verse in verses[:-1]:
        result.extend(verse)
        result.append("")
    result.extend(verses[-1])

    return result


def _pluralize_bottle(number) -> str:
    if number == 1:
        return "bottle"
    return "bottles"
