from factory_a import FactoryA
from factory_b import FactoryB


class AbstractFactory:
    @staticmethod
    def get(name):
        if name[0] == "a":
            return FactoryA().get_product(name[1])
        elif name[0] == "b":
            return FactoryB().get_product(name[1])
        else:
            raise ValueError(f"product {name} doesnt exist!")

