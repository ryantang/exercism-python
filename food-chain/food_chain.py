"""Recite verses of 'I Know an Old Lady Who Swallowed a Fly'."""

COMMENTARY = [
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!",
    "She's dead, of course!",
]

ANIMALS = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
DESCRIPTIONS = {"spider": "spider that wriggled and jiggled and tickled inside her"}
FLY_INDEX = 0
HORSE_INDEX = 7

def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite the song 'I know an old lady who swallowed a fly'."""
    lyrics = []
    for verse_index in range(start_verse - 1, end_verse):
        lyrics += _compose_verse(verse_index)
        if verse_index < end_verse - 1:
            lyrics.append("")

    return lyrics

def _compose_verse(verse_index: int) -> list[str]:
    """Return the lines of one verse."""
    if verse_index in (FLY_INDEX, HORSE_INDEX):
        return [_opening(verse_index), COMMENTARY[verse_index]]

    food_chain = [_reason(index) for index in range(verse_index, -1, -1)]
    return [_opening(verse_index), COMMENTARY[verse_index], *food_chain]

def _opening(verse_index: int) -> str:
    """Return the opening line of a verse for the given animal."""
    return f"I know an old lady who swallowed a {ANIMALS[verse_index]}."

def _reason(verse_index: int) -> str:
    """Return return the reason the old lady swallowed an animal."""
    if verse_index == FLY_INDEX:
        return COMMENTARY[FLY_INDEX]

    predator = ANIMALS[verse_index]
    prey = ANIMALS[verse_index - 1]
    prey_description = DESCRIPTIONS.get(prey, prey)
    return f"She swallowed the {predator} to catch the {prey_description}."
