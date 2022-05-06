from abc import ABCMeta , abstractmethod


class IComponent(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method():
        ...

