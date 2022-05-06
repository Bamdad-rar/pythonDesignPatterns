

"Sometimes you need an object in an application where there is only one instance.

By creating a class and following the Singleton pattern, you can make sure that even if any number of
instances were created, they will still refer to the original class.

The Singleton can be accessible globally, but it is not a global variable. It is a class that can be
instanced at any time, but after it is first instanced, any new instances will point to the same instance
as the first.
For a class to behave as a Singleton, it should not contain any references to self but use static
variables, static methods and/or class methods"

     -Design Patterns In Python by Sean Bradley


there are multiple approaches to creating a Singleton in python, some even consider it an Anti-Pattern.


so to elaborate on the use cases of Singleton pattern, it can be used to:
     1. to create a single object that maintains a global state of our program.
     2. controlling concurrent access to a shared file or resource. (for example an object that manages the connection to a database)
     3. A service or a resource that is transversal, meaning it can be used by different parts of the program and by different users.

