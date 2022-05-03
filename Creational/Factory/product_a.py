from product_interface import IProduct


class ProductA(IProduct):
    """product a"""
    def __init__(self):
        self.name = "product a"
        self.length = 10
        self.width = 20
        self.height = 30

    def get_repr(self):
        return f"product name : {self.name}; dimensions : ({self.length},{self.width},{self.height})"
