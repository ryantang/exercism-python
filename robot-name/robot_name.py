import random, string

class Robot:
    def __init__(self):
          self.used_names = set()
          self.name = self._generate_name()
          self.used_names.add(self.name)

    def name(self):
        return self.name
    
    #factory reset wipes the old name and creates a new one
    def reset(self):
        new_name = self._generate_name()

        while new_name in self.used_names:
            new_name = self._generate_name()
        
        self.name = new_name
        self.used_names.add(new_name)
    
    @staticmethod
    def _generate_name():
        prefix = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        suffix = ''.join(random.choice(string.digits) for _ in range(3))
        return (prefix + suffix)
