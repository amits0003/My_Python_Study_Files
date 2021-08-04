from collections import *

squares1 = []

for x in range(10):
    squares1.append(x**2)

print('squares set by type 1',squares1)

squares2 = []
squares2 = list(map(lambda x: x**2, range(10)))

print('squares set by type 2',squares2)

squares3 = [x**2 for x in range(10)]

print('squares set by type 3',squares3)

squares4 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

print ('sqaure of type 4 ', squares4)

sqaure5 = []

for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            sqaure5.append((x,y))

print('Sqaure of type 5 ', sqaure5)
