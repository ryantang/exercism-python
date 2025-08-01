ORDINALS = [
    'zeroth', 
    'first', 
    'second', 
    'third', 
    'fourth', 
    'fifth', 
    'sixth', 
    'seventh', 
    'eighth', 
    'ninth', 
    'tenth', 
    'eleventh', 
    'twelfth'
    ]
GIFTS = [
    '', #zeroth day
    'a Partridge in a Pear Tree.', 
    'two Turtle Doves, ', 
    'three French Hens, ', 
    'four Calling Birds, ',
    'five Gold Rings, ',
    'six Geese-a-Laying, ',
    'seven Swans-a-Swimming, ',
    'eight Maids-a-Milking, ',
    'nine Ladies Dancing, ',
    'ten Lords-a-Leaping, ',
    'eleven Pipers Piping, ',
    'twelve Drummers Drumming, '
]

def recite(start_verse, end_verse):
    return [get_verse(day) for day in range(start_verse, end_verse + 1)]


def get_verse(verse):
    first = [f'On the {ORDINALS[verse]} day of Christmas my true love gave to me: ']
    middle = GIFTS[verse:1:-1]
    if verse > 1:
        last = ['and ' + GIFTS[1]]
    else:
        last = GIFTS[1:2]
    
    return ''.join(first + middle + last)


