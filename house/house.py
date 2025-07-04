PARTS = [
    'the house that Jack built.',
    'the malt that lay in',
    'the rat that ate',
    'the cat that killed',
    'the dog that worried',
    'the cow with the crumpled horn that tossed',
    'the maiden all forlorn that milked',
    'the man all tattered and torn that kissed',
    'the priest all shaven and shorn that married',
    'the rooster that crowed in the morn that woke',
    'the farmer sowing his corn that kept',
    'the horse and the hound and the horn that belonged to'
]
PREFIX = 'This is'

def recite(start_verse, end_verse):

    return [
        _build_verse(verse)
        for verse in range(start_verse, end_verse + 1)
    ]

def _build_verse(verse):
    verse_parts = " ".join(PARTS[verse -1::-1])
    return f'{PREFIX} {verse_parts}'

