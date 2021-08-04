# x = {'mon':1,'tue':2, 'wed':2}
# 
# a_list = ['name1', 'name2', 'name1', 'name3']
# new_dict = dict()
# 
# for name in a_list:
#     new_dict[name] = new_dict.get(name, 0) + 1
# 
# print(new_dict)
# 
# for key, v in new_dict.values():
#     print('key' , v)
#     #print('value', value)

 #create an empty dictionary
counts = dict()
new_dict = {}
line = input("Enter a line of Text : ")

#Generate a list out of it.
words = line.split()

print('words is of type: ',type(words))

print("The index and the value at index in the list are :")
for index, value in enumerate(words):
    print('index: ', index,', value : ',value)
    
print('The list generated is as  : ', words)

print("----------------------------------------------------")

#Generating a dictionary from List using get.
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('counts is of type: ',type(counts))
print('The Dictionary generated is as : ', counts)

print('Key and Value pairs are : ')
for key, values in counts.items():
    print('key: ', key, ', value: ', values)
    
print("----------------------------------------------------")
#Generating dict from list using conventional way

for word in words:
    if word in new_dict:
        new_dict[word] = new_dict[word]+1
    else:
        new_dict[word] = 1

print("Generating Dict through conventional approach : ", new_dict)

print("----------------------------------------------------")
    