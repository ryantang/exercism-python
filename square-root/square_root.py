def square_root(number):
    return newtons_method(1, number)
    # return linear_search(number)
    # return binary_search(0, number + 1, number)


def newtons_method(guess, number):
    if guess * guess == number:
        return guess

    new_guess = 0.5 * (guess + number/guess)

    return newtons_method(new_guess, number)

def linear_search(number):
    for estimate in range(0, number + 1):
        if estimate * estimate == number:
            return estimate
        
    raise ValueError(f'{number} does not have an integer square root')

def binary_search(lower, upper, number):
    guess = (lower + upper) // 2
    square_of_guess = guess * guess

    if square_of_guess == number:
        return guess
    elif square_of_guess > number:
        return binary_search(lower, guess + 1, number)
    elif square_of_guess < number:
        return binary_search(guess, upper, number)
    
