def distance(strand_a, strand_b):
    length = len(strand_a)
    if length != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    
    mismatches = (
        a != b
        for a, b in zip(strand_a, strand_b)
    )

    return sum(mismatches)

