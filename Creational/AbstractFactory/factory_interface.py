from abc import ABCMeta, abstractmethod


class IFactory(metaclass=ABCMeta):
    """ interface for the factories """

    @staticmethod
    @abstractmethod
    def get_product():
        """factories handle the product fetching"""


