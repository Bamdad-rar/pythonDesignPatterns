from product_interface import IProduct


class ProductA2(IProduct):
    def __init__(self):
        self.name = "product A 2"
    def get_repr(self):
        return self.name


