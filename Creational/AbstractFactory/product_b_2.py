from product_interface import IProduct


class ProductB2(IProduct):
    def __init__(self):
        self.name = "product B 2"
    def get_repr(self):
        return self.name


