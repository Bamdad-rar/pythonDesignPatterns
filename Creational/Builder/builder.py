from builder_interface import IBuilder
from product import Product

class Builder(IBuilder):
    def __init__(self):
        self.product = Product()


    def build_part_a(self):
        self.product.parts.append("part a")
        return self

    def build_part_b(self):
        self.product.parts.append("part b")
        return self

    def build_part_c(self):
        self.product.parts.append("part c")
        return self

    def get_result(self):
        return self.product


