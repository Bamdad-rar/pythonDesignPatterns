from product_a import ProductA
from product_b import ProductB
from product_c import ProductC


class ProductFactory:
    @staticmethod
    def get_product(name):
        if name == "product_a":
            return ProductA()
        elif name == "product_b":
            return ProductB("coming soon...")
        elif name == "product_c":
            return ProductC()
        else:
            raise ValueError("product doesnt exist")

