from abc import ABCMeta, abstractmethod



class IProduct(metaclass=ABCMeta):
    """interface for the products"""
    
    @staticmethod
    @abstractmethod
    def get_repr():
        """returns a representation of the product"""
        ...

