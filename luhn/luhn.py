class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def valid(self) -> bool:
        if len(self.card_num) <= 1:
            return False
        
        if not all(char.isdigit() for char in self.card_num):
            return False
        
        card_digits = [int(i) for i in self.card_num]

        #transform every second digit, moving backwards from the end of the list
        for i in range(len(card_digits)-2, -1, -2):
            card_digits[i] = self._transform(card_digits[i])

        return sum(card_digits) % 10 == 0
    
    @staticmethod
    def _transform(digit):
        doubled = digit * 2
        return doubled - 9 if doubled > 9 else doubled