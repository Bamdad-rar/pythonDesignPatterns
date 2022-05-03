from product_interface import IProduct


class ProductB1(IProduct):
    def __init__(self):
        self.name = "product B 1"
    def get_repr(self):
        return self.name


