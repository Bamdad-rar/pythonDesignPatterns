from copy import deepcopy



class Prototype:
    def __init__(self):
        self.objects = {}
    
    
    def register(self,identifier,obj):
        self.objects[identifier] = obj
        return self
    
    def unregister(self,identifier):
        if identifier in self.objects:
            del self.objects[identifier]
        else:
            raise AttributeError(f'{identifier} does not exist')
        return self
        
    def clone(self,identifier,**attrs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f"{identifier} does not exist")
        
        obj = deepcopy(found)
        
        for item in attrs:
            setattr(obj, item, attrs[item])
            
        return obj


