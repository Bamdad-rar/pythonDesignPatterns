from component_interface import IComponent
from component import Component

class Decorator(IComponent):
    def __init__(self,obj):
        self.obj = obj

    def method(self):
        print("doing something before the main thing")
        self.obj.method()
        print("and doing something extra after the thing")

