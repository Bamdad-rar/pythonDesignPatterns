from abc import abstractmethod,ABCMeta


class IValue(metaclass=ABCMeta):
    
    @abstractmethod
    def __str__():
        """returns the string representation of the value"""

