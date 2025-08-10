def roman(number, accumulator=''):
    if number > 3_999 or number < 0:
        raise ValueError("Please provide a number between 1 and 3,999")
    
    if not number and not accumulator:
        raise ValueError("Please provide a number between 1 and 3,999")

    if number == 0:
        return accumulator

    if number >= 1000:
        return roman(number - 1000, accumulator + 'M')
    if number >= 900:
        return roman(number - 900, accumulator + 'CM')
    if number >= 500:
        return roman(number - 500, accumulator + 'D')
    if number >= 400:
        return roman(number - 400, accumulator + 'CD')
    if number >= 100:
        return roman(number - 100, accumulator + 'C')
    if number >= 90:
        return roman(number - 90, accumulator + 'XC')
    if number >= 50:
        return roman(number - 50, accumulator + 'L')
    if number >= 40:
        return roman(number - 40, accumulator + 'XL')
    if number >= 10:
        return roman(number - 10, accumulator + 'X')
    if number >= 9:
        return roman(number - 9, accumulator + 'IX')
    if number >= 5:
        return roman(number - 5, accumulator + 'V')
    if number >= 4:
        return roman(number - 4, accumulator + 'IV')
    if number >= 1:
        return roman(number - 1, accumulator + 'I')


    

