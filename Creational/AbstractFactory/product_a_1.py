from product_interface import IProduct


class ProductA1(IProduct):
    def __init__(self):
        self.name = "product A 1"
    def get_repr(self):
        return self.name


