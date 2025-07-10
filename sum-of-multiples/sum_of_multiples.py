def sum_of_multiples(limit, multiples):
    values = set()
    for multiple in multiples:
        if multiple == 0:
            continue
        for value in range(0, limit, multiple):
            values.add(value)
    
    return sum(values)
