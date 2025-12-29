def primes(limit):
    number_list = [False] * 2 + [True] * (limit - 1)
    for i in range(2,limit + 1):
        j = 2
        while i * j <= limit:
            print(f'i*j is {i*j}')
            number_list[i*j] = False
            j = j+1

    print(f'number_list is {number_list}')
    return [index for index, value in enumerate(number_list) if value]
