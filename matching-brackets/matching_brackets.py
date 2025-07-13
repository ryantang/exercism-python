MATCHING_PAIRS = {
    '[': ']',
    '{': '}',
    '(': ')'
}

OPENERS = "[({"
CLOSERS = "])}"

def is_paired(input_string):
    open_stack = []

    for char in input_string:
        if char in OPENERS:
            open_stack.append(char)
        elif char in CLOSERS:
            if not open_stack:
                return False

            opener = open_stack.pop()
            if not MATCHING_PAIRS.get(opener) == char:
                return False

    return not open_stack
