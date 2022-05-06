
abstract factory creates another layer of abstraction over multiple other creational patterns

a factory that can return factories

it can also return
    builder,prototype,singleton, or other design pattern implementations




Client:
    the dude that calls the abstract factory

Abstract factory:
    a common interface over all of the sub factories


Concrete factory:
    the sub factory of the abstract factory, contains the methods for creating concrete products


Abstract Product:
    the interface for the products that the factories use.


Concrete Product:
    the implementations of the product (object) that will be returned by the factories


