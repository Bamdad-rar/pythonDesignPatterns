from value_interface import IValue


class Value(IValue):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
