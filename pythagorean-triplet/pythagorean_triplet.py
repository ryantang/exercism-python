SMALLEST_PYTHAGOREAN_TRIPLET_LEG = 3

def triplets_with_sum(number):
    triplets = []

    c_min = number // 3
    c_max = number // 2
    for c in range(c_min, c_max + 1):
        if number - c <= c:
            break

        c_squared = c ** 2
        a_min = max(SMALLEST_PYTHAGOREAN_TRIPLET_LEG, 2 * c - number + 1)
        a_max = min(c - 1, (number - c) // 2)
        for a in range(a_min, a_max + 1):
            b = number - a - c
            if a ** 2 + b ** 2 == c_squared:
                triplets.append([a, b, c])
    
    return triplets
