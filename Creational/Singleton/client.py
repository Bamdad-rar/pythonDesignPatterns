from singleton import MySingleton
import copy


s1 = MySingleton()
print(id(s1))

s2 = copy.deepcopy(s1)
print(id(s2))

s3 = MySingleton()
print(id(s3))

