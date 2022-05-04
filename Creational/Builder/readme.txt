

Product:
    the thing/object/product being built

Builder Interface:
    the interface that the concrete builder should implement

Builder:
    provides methods to build and retrieve the concrete product
    this implements the buidler interface

Director:
    this guy has a construct method that when called creates a
    customized product using the methods provided by the builder.


this setup enables you to have different directors for differently composed objects.

for example one director can have the parts built in a particular order and another
director can have some parts not built into the object.


