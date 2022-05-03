from factory_interface import IFactory
from product_b_1 import ProductB1
from product_b_2 import ProductB2



class FactoryB(IFactory):

    @staticmethod
    def get_product(product_name):
        if product_name == "1":
            return ProductB1()
        elif product_name == "2":
            return ProductB2()
        else:
            raise ValueError("product doesnt exist...")


