from abc import ABCMeta , abstractmethod


class IBuilder(metaclass=ABCMeta):
    """interface for the builder class"""
    @staticmethod
    @abstractmethod
    def build_part_a():
        ...

    @staticmethod
    @abstractmethod
    def build_part_b():
        ...

    @staticmethod
    @abstractmethod
    def build_part_c():
        ...



