VERSES = [
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!",
    "She's dead, of course!",
]

SPIDER_DESC = "spider that wriggled and jiggled and tickled inside her"
ANIMALS = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse" ]
ANIMAL_DESC = ["fly", SPIDER_DESC, "bird", "cat", "dog", "goat", "cow", "horse"]

def recite(start_verse, end_verse):
    lyrics = []
    for verse_number in range(start_verse, end_verse + 1):
        lyrics += _compose_verse(verse_number)
        _add_blank_line_between_verses(lyrics, verse_number, end_verse)

    return lyrics

def _add_blank_line_between_verses(lyrics, verse_number, end_verse):
    if verse_number < end_verse:
        lyrics.append("")

def _compose_verse(verse_number):
    if verse_number == 1:
        return [opening(0), VERSES[0]]
    if verse_number == 8:
        return [opening(7), VERSES[7]]


    start_idx = verse_number - 1
    lyrics = [opening(start_idx), VERSES[start_idx]]
    for i in range(start_idx -1, -1, -1):
        lyrics.append(transition(i))
    lyrics.append(VERSES[0])
    return lyrics

def opening(verse_idx):
    return f"I know an old lady who swallowed a {ANIMALS[verse_idx]}."

def transition(verse_idx):
    return f"She swallowed the {ANIMALS[verse_idx+1]} to catch the {ANIMAL_DESC[verse_idx]}."
