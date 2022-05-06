from value_interface import IValue



class Del(IValue):
    def __init__(self,x,y):
        x = getattr(x,'value', x)
        y = getattr(y,'value', y)
        self.value = x-y
        
    def __str__(self):
        return str(self.value)


