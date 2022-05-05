

prototype is used when you have an object in memory, and you want another version of it but you cant change the original one.
the solution here is to make a clone of it.
now you might say why not create another one of those objects instead of cloning/copying it?
some objects take too much time to build or take too much resources. for example getting an object from database might
be very expensive in some cases, so you cant simply create the object hence the cloning.

now that the solution is clear, the only thing remaining is the how. this is where the prototype design pattern comes in handy.
and further more because of built-in deepcopy functionality, this pattern is super easy in python.


