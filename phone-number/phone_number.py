import re
import string

class PhoneNumber:
    def __init__(self, number):
        self._number = self.standardize(number)

    @property
    def number(self):
        return self._number
    
    @property
    def area_code(self):
        return self._number[:3]
    
    def pretty(self):
        exchange = self._number[3:6]
        subscriber = self._number[6:]
        return f'({self.area_code})-{exchange}-{subscriber}'
    
    @staticmethod
    def standardize(number):
        cleaned = re.sub(r'[ -.()]','', number)

        if any(digit in string.ascii_letters for digit in cleaned):
            raise ValueError("letters not permitted")
        if any(digit in string.punctuation for digit in cleaned):
            raise ValueError("punctuations not permitted")

        if len(cleaned) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(cleaned) == 11:
            if cleaned[0] == '1':
                cleaned = cleaned[1:]
            else:
                raise ValueError("11 digits must start with 1")
        if len(cleaned) > 11:
            raise ValueError("must not be greater than 11 digits")
        
        if cleaned[0] == '0':
            raise ValueError("area code cannot start with zero")
        if cleaned[0] == '1':
            raise ValueError("area code cannot start with one")
        if cleaned[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        if cleaned[3] == '1':
            raise ValueError("exchange code cannot start with one")
        
        return cleaned