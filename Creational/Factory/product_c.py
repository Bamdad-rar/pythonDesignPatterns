from product_interface import IProduct


class ProductC(IProduct):
    """product c has hard coded values"""
    def __init__(self):
        self.name = "Product C"

    def get_repr(self):
        return self.name
