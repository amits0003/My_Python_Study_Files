
print("Begining of a new Python File")

x,y,z  = input("Enter integer, float and string following by comma").split(',')

str = x+'$'+y+'$'+z+'$'
str1 = str.strip(' ')
print(str1)
print(f"{x}${y}${z}$".format())

print('{0}${1}${2}$'.format(x,y,z))
x = int(x)
y = float(y)
print("%d$%.2f$%s$"%(x,y,z))
