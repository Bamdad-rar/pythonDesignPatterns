from abc import ABCMeta,abstractmethod


class IProduct(metaclass=ABCMeta):

    @abstractmethod
    def get_repr():
        ...

