from product_interface import IProduct


class ProductB(IProduct):
    """product b gets input at initialization"""
    def __init__(self, comment):
        self.name = "product b"
        self.comment = comment

    def get_repr(self):
        return f"{self.name} ; product comment : {self.comment}"