a = 5
b = 6
c = 4.55
d = 'str'

print(1,a>b)
print(2,a<b)
print(3,a!=b)
print(4,b<a)
print(5,b>a)

print(6,a<b and b>c)
print(7,a<b or b>c)

a = {1,2,3}

print(type(a))

# misc examples

fruit = {1: 'AMit'}

x  = {x for x in fruit.keys()}

print(type(x))