from value import Value
from add_decorator import Add
from del_decorator import Del


A = Value(10)
B = Value(20)
C = Value(30)


print(Add(A,B)) # res : 30
print(Add(A,C)) # res : 40
print(Add(A,10)) # res : 20
print(Del(A,C)) # res : -20

