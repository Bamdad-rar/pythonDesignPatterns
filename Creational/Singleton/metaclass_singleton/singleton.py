

class SingletonType(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # what happens here is that, we are calling super() which points to 
            # the superclass type
            # type can create classes, infact its python's way of creating classes
            # under the hood
            # when we invoke __call__ on type two more functions will be called
            # __new__ and __init__. 
            cls._instances[cls] = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
    