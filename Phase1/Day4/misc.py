'''this program will use different approach to see different programs'''
from pip._internal import self_outdated_check

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return 'Vector (%d %d)' % (self.a, self.b)
    
    def __add__(self,other):
        return (self.a + other.a, self.b+other.b)
    
v1 = Vector(2,10)
v2 = Vector(5,-1)

print(v1+v2)
    