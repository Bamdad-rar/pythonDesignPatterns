from product_factory import ProductFactory

"""
this patterns gives us the ability to create objects dynamically at runtime!
here I am getting the object name that should be created from the user, which is pretty cool.
"""

product_name = input()

print(ProductFactory().get_product(product_name).get_repr())

