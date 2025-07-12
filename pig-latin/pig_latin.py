VOWELS = 'aeiou'

def translate(text):
    translated = [
        translate_word(word)
        for word in text.split()
    ]

    return ' '.join(translated)
        

def translate_word(text):
    if not text.isalpha():
        raise(ValueError(f'Only letters allowed. Input: {text}'))

    if text[0] in VOWELS:
        return text + 'ay'
    if text[0:2] == 'xr' or text[0:2] == 'yt':
        return text + 'ay'
    
    # When the word begins with one or more constanants
    leading_consonants = ''
    for index, letter in enumerate(text):

        # Handle special case of 'qu'
        if letter == 'u' and leading_consonants.endswith('q'):
            remaining_letters = text[index + 1:] # After 'qu'
            return remaining_letters + leading_consonants + 'u' + 'ay'
        
        # When we've gathered leading consonants and hit a vowel
        if letter in VOWELS:
            remaining_letters = text[index:] # starting from the vowel
            return remaining_letters + leading_consonants + 'ay'
        
        # Handle 'y' when it comes after one or more constatanants
        if letter == 'y' and leading_consonants:
            remaining_letters = text[index:] #starting from the first 'y'
            return text[index:] + leading_consonants + 'ay'
            
        leading_consonants += letter


    
    
    

