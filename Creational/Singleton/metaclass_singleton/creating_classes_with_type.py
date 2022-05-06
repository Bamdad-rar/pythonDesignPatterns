

class T:
    ...


# we can define a class A with
# type(classname, superclasses, attributedict)
A = type('A',(),{})

# When we call "type", the call method of type is called. The call method runs two other methods: new and init:
# type.__new__(typeclass, classname, superclasses, attributedict)
# type.__init__(cls, classname, superclasses, attributedict)
# The new method creates and returns the new class object, and after this, the init method initializes the newly created object.

if __name__ == '__main__':
    print(T().__class__)
    print(A().__class__)
    