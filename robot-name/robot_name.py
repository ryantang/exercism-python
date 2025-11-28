import random
import string

class Robot:
    _used_names = set()

    def __init__(self):
        self._name = Robot._unique_name()

    @property
    def name(self):
        return self._name
    
    #factory reset wipes the old name and creates a new one
    def reset(self):        
        self._name = Robot._unique_name()
    
    @classmethod
    def _unique_name(cls):
        new_name = cls._generate_name()

        while new_name in cls._used_names:
            new_name = cls._generate_name()
        
        cls._used_names.add(new_name)
        return new_name

    @staticmethod
    def _generate_name():
        prefix = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        suffix = ''.join(random.choice(string.digits) for _ in range(3))
        return (prefix + suffix)
