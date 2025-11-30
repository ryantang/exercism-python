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
        exchange_code = self._number[3:6]
        subscriber_num = self._number[6:]
        return f'({self.area_code})-{exchange_code}-{subscriber_num}'
    
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
            country_code = cleaned[0]
            if country_code != '1':
                raise ValueError("11 digits must start with 1")
            
            cleaned = cleaned[1:] #PhoneNumber doesn't currently store country code
        if len(cleaned) > 11:
            raise ValueError("must not be greater than 11 digits")
        
        area_code_start = cleaned[0]
        if area_code_start == '0':
            raise ValueError("area code cannot start with zero")
        if area_code_start == '1':
            raise ValueError("area code cannot start with one")
        
        exchange_code_start = cleaned[3]
        if exchange_code_start == '0':
            raise ValueError("exchange code cannot start with zero")
        if exchange_code_start == '1':
            raise ValueError("exchange code cannot start with one")
        
        return cleaned