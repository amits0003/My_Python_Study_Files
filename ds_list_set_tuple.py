listA = [1,2,3,4]
tupA = tuple(listA)
dict_example1 = {tupA:"Amit", (2,):"Sumit", '2': 'Field', 2: 1212}

strA = str(listA)

dict_example2 = {strA:"Amit", (2,) : "Sumit" , '2': 'Field', 2: 1212}

print('dictionary example 1 :',dict_example1)

print('dictionary example 2 :',dict_example2)

for index in dict_example2.items() :
    print(index)
for index in dict_example1.items():
    print(index)

keyList = [1,2,3,4,5]

varDict = dict.fromkeys(keyList)

print(varDict)

varDict1 = dict.fromkeys(keyList,[])

fNameList = ['Amit','Sumit']
lNameList = ['Kumar','Kr']

zipVar = zip(fNameList,lNameList)
print(zipVar)
print(list(zipVar))
print(dict(zip(fNameList,lNameList)))
