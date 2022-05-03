from factory_interface import IFactory
from product_a_1 import ProductA1
from product_a_2 import ProductA2



class FactoryA(IFactory):

    @staticmethod
    def get_product(product_name):
        if product_name == "1":
            return ProductA1()
        elif product_name == "2":
            return ProductA2()
        else:
            raise ValueError("product doesnt exist...")


