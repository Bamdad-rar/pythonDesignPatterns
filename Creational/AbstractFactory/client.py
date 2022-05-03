from abstract_factory import AbstractFactory


product_name = input()

try:
    temp = AbstractFactory().get(product_name).get_repr()
except Exception as _e:
    print(f"error: {_e}")
else:
    print(temp)
